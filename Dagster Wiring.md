## 1. Dagster Wiring System — Core Principles

Dagster composes functions declaratively.
Each `@op` is an isolated unit of work; a `@job` connects them into a dependency graph.
All configuration, data flow, and resources must be explicitly wired.

---

### Op Wiring

Each op defines inputs and outputs:

```python
@op(ins={"input_name": In(InputType)}, out=Out(OutputType))
def my_op(context, input_name):
    ...
```

Job composition:

```python
@job
def example_job():
    op_b(op_a())
```

Dagster does not infer wiring. Every input must be connected to an output or be `Nothing`.

---

### “Nothing” Inputs for Control Flow

Use `Nothing` to enforce order without passing data:

```python
@op(out=Out(Nothing))
def prepare_op(_):
    print("Prep done")

@op(ins={"start": In(Nothing)})
def main_op(_):
    print("Main work")

@job
def pipeline():
    main_op(prepare_op())
```

`main_op` executes after `prepare_op`.

---

### Resources

Resources are shared context objects defined separately and injected at runtime.

```python
@resource(config_schema={"yaml_path": str})
def machine_config_resource(init_context):
    import yaml, pathlib
    path = pathlib.Path(init_context.resource_config["yaml_path"]).expanduser()
    return yaml.safe_load(path.open())

@op(required_resource_keys={"machine_config"})
def example_op(context):
    config = context.resources.machine_config
```

Resources are initialized once per process and accessed via `context.resources.<name>`.

---

### Resource Dependencies

Resources can depend on other resources:

```python
@resource(required_resource_keys={"machine_config"})
def gcp_credentials(init_context):
    from google.oauth2 import service_account
    cfg = init_context.resources.machine_config
    return service_account.Credentials.from_service_account_file(
        cfg["gcp_service_account_key_path"]
    )
```

Attach both:

```python
@job(resource_defs={
    "machine_config": machine_config_resource,
    "gcp_credentials": gcp_credentials
})
def gcloud_pipeline():
    ...
```

Gotcha: Each dependent resource must declare `required_resource_keys`, or Dagster will raise a definition error.

---

## 2. Example: GCP Machine Control

Ops:

```python
@op(out=Out(Nothing))
def authenticate_gcloud_op(context):
    result = authenticate_gcloud(...)
    context.log.info("GCP authentication successful." if result else "Failed.")

@op(required_resource_keys={"machine_config", "gcp_credentials"}, out=Out(list))
def list_gcloud_machines_op(context):
    creds = context.resources.gcp_credentials
    project_id = context.resources.machine_config["gcp_project_id"]
    return list_gcloud_machines(project_id, creds)

@op(ins={"machines": In(list)}, out=Out(list))
def start_machine_op(context, machines):
    ...
```

Job wiring:

```python
@job(resource_defs={"machine_config": machine_config_resource,
                    "gcp_credentials": gcp_credentials})
def gcloud_pipeline():
    auth = authenticate_gcloud_op()
    machines = list_gcloud_machines_op()
    start_machine_op(machines)
```
---
## 3. Repository Setup for Multiple Jobs

Multiple jobs require a repository:

```python
from dagster import repository
from .gcloud_pipeline import gcloud_pipeline
from .gcloud_stop_pipeline import gcloud_stop_pipeline

@repository
def gcloud_repo():
    return [gcloud_pipeline, gcloud_stop_pipeline]
```

Run with:

```bash
dagster job execute -m gcloud_repo -j gcloud_pipeline
```

---

## 6. Toy Example

```python
from dagster import op, job, In, Out

@op(out=Out(str))
def produce(context):
    context.log.info("Producing data")
    return "Hello Dagster"

@op(ins={"msg": In(str)})
def consume(context, msg):
    context.log.info(f"Consumed: {msg}")

@job
def hello_job():
    consume(produce())
```

Run:

```bash
dagster job execute -f hello.py -j hello_job
```


Dagster builds a static execution graph from declarative function wiring and validates all dependencies, configurations, and types before execution.

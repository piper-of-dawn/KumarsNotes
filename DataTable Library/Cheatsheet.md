## Filtering and Grouping
```
df = Frame(data_dict.get('df1')[['col1', 'col2']])[0, :, by('col1')]
```
`Frame(...)[0, :, by('col1')]`: The resulting data table from step 2 is wrapped in the `Frame()` function to convert it back to a `datatable.Frame` object. Then, the following operations are applied to this frame:
    
 `[0, :]` selects the first row (index 0) and all columns from the frame. This operation filters the data table to only include the first row.
        
 `by('col1')` groups the data by the values in the `'col1'` column. This operation groups the datatable based on unique values in the `'col1'` column.

df = df[:, :, join(df1)]
`[:, :, join(df1)]`: This part specifies the join operation between `df` (left table) and `df1` (right table). Here's what each component means:

- `[:, :]`: The first colon (`:`) represents all rows, and the second colon (`:`) represents all columns. This selection specifies that you want to include all rows and columns from the left table (`df`).
    
- `join(df1)`: The `join()` function is used to perform a join operation between two tables. In this case, `df1` is the right table that you want to join with `df`. By specifying `join(df1)`, you are instructing the `join()` function to perform a join between the left table (`df`) and the right table (`df1`).


df = another_df[:, {'col1': f.col1}]

`[:, {'col1': f.col1}]`: This part specifies the selection of columns from `another_df`. Here's what each component means:

- `[:, ...]`: The first colon (`:`) represents all rows, and the ellipsis (`...`) indicates that all rows are selected. This selection specifies that you want to include all rows from `another_df`.
    
- `{'col1': f.col1}`: This dictionary specifies the columns you want to select. In this case, you are selecting the `'col1'` column from `another_df`. The key `'col1'` represents the name of the column in the new datatable (`df`), and `f.col1` refers to the column named `'col1'` in `another_df`. The `f.col1` expression is used to reference the column `'col1'` from the original datatable.



 
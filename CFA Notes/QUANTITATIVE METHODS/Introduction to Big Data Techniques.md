r# Introduction to Big Data Techniques

> [!ABSTRACT] LOS
> 1. Describe the parts of fintech that matter for gathering and analyzing financial data.
> 2. Describe Big Data, artificial intelligence, and machine learning.
> 3. Describe applications of Big Data and data science to investment management.

> [!tip] SEE THIS BEFORE EXAM
> - Fintech here is not "all finance apps on Earth." For this reading, care about two things: **huge data** and **tools that can process those data faster and better than old workflows**.
> - Big Data = **volume + velocity + variety**, and when the question is about prediction or inference, add **veracity**. If a dataset is massive, arrives every second, and includes text, images, and transaction feeds, that is Big Data. If the source is sketchy, the fourth V is the real trap.
> - Structured data fit rows and columns. Semistructured data have some organization but not fully clean tables. Unstructured data are messy things like voice, video, email, and social posts. If the question says "earnings call audio" or "tweets," think **unstructured**.
> - Alternative data are non-traditional data used for investment insight. If the data come from **people**, think clicks, reviews, browsing, posts. If they come from **business processes**, think card swipes, scanner sales, shipping records. If they come from **sensors**, think satellites, GPS, traffic, geolocation.
> - If a model gets training data almost perfectly right and then looks stupid on new data, that is **overfitting**.
> - If the algorithm gets inputs plus known answers during training, it is **supervised learning**. If it gets data with no labels and is told to discover groupings or structure, it is **unsupervised learning**.
> - Deep learning is just machine learning using neural networks with many hidden layers. Do not over-romanticize it. On the exam, it is still a pattern-learning tool.
> - Text analytics is the big bucket. Natural language processing sits inside it. If the task is reading filings, transcripts, central-bank speeches, or employee emails, think **text analytics / natural language processing**, not generic machine learning in the abstract.
> - Low latency means low delay. If the question involves real-time trading, market-making, or reacting instantly to market data, low latency is the system feature that matters.
> - ==Huge data are useless if they are biased, dirty, illegally obtained, or irrelevant. Big Data does not cancel bad judgment.==

1. This module is basically about finance getting flooded with data and needing new tools to survive that flood.
2. It starts with fintech. What is fintech: technology-driven innovation in financial services and financial products. In normal conversation, fintech can also mean the firms building those tools, but for the exam the useful angle is what the technology is doing.
3. At first, technology in finance mostly automated routine tasks. Then systems started following explicit rule books. Now some systems learn patterns from data and support or automate more complex decisions.
4. That matters in investment management because analysts now face far more information than older human-only workflows were designed to handle. The curriculum cares especially about two things: access to large datasets and analytical tools that can handle those datasets.
5. Traditional data include prices, volumes, financial statements, economic releases, annual reports, regulatory filings, and earnings calls.
6. Alternative data mean non-traditional data that can still help an investment decision. Examples include web traffic, social media, geolocation, emails, satellite imagery, scanner data, and company exhaust.

7. What is company exhaust: data created as a by-product of normal business activity. Why this matters: sometimes the useful signal appears in the exhaust before it appears in the official report.

> [!example] THE MACHINE READS BEFORE THE ANALYST DOES
> Earnings season is a perfect stress test. Humans can read some filings and hear some calls. A machine can scan every filing, every transcript, every wording shift, and flag where management tone changed before a tired analyst has even finished the second coffee.

8. Big Data means more than size. What is Big Data: extremely large, fast-moving, and varied datasets that usually need special methods to capture, store, search, and analyze.
9. The classic three Vs are volume, velocity, and variety. Volume means a huge amount of data. Velocity means the data arrive or move very quickly, sometimes in real time or near real time. Variety means the data come in many forms rather than one clean spreadsheet structure.
10. For prediction and inference,add a fourth V: veracity. What is veracity: whether the data are credible, reliable, and truthfully reflecting the thing you think they reflect.
11. This is the exam maturity point. Big Data can magnify bad data just as efficiently as good data.
12. Data can be structured, semistructured, or unstructured. Structured data fit neatly into tables where each field has a consistent meaning. Semistructured data have some organization but do not sit cleanly in a standard table. Unstructured data are messy things like emails, voice, images, video, and free text.
13. Why this classification matters: structured data are easier to store and analyze with old-school database tools, while unstructured data usually need extra processing before they become useful.

> [!TIP] HAMMER THIS INTO YOUR HEAD
> - If a question mentions rows and columns, think structured.
> - If it mentions tags or markup-like organization but not clean tables, think semistructured.
> - If it mentions human language, audio, pictures, or video, think unstructured.
> 

8. The curriculum groups Big Data origins into financial markets, businesses, governments, individuals, and sensors.
	- Financial-market data include equity, fixed income, futures, options, and derivative activity.
	- Business data include transactions, supply-chain records, point-of-sale data, and internal operating information.
	- Government data include employment, trade, payroll, and macroeconomic releases.
9. Individual-generated data include search histories, reviews, clicks, and social posts.
10. Sensor-generated data include satellites, shipping trackers, traffic flows, and geolocation. The Internet of Things belongs inside this sensor world. What is the Internet of Things: connected physical devices with sensors and software that collect and transmit data.

> [!example] 
>  Suppose you are using the satellite imagery of McDonald's parking lots to forecast revenue for McDonald's. That is how alternative data is used.

11. Alternative data are a narrower investment-use idea inside the wider Big Data story. What are alternative data: non-traditional data used to support investment analysis or investment decisions.
12. The curriculum sorts them into data generated by **individuals, business processes, and sensors**. Data from individuals are often unstructured.
13. Data from business processes are often structured and can act like leading or real-time indicators. What is a leading indicator here: information that hints at performance before the normal accounting reports arrive. Sensor data can be enormous in scale and update frequency.
14. Investors use alternative data to improve research, improve trade execution, identify factors affecting prices, and spot trends earlier.

> [!question] IDENTIFY THE DATA TYPE
> Problem: Classify each item as structured, semistructured, or unstructured.
>
> 9. A database of daily bond yields in rows and columns.
> 10. Earnings call audio files.
> 11. Web pages with tags and some internal structure but inconsistent formatting.
>
> ---
>
> Solution:
>
> 12. Daily bond-yield database = **structured**.
> 13. Earnings call audio = **unstructured**.
> 14. Tagged but inconsistently formatted web pages = **semistructured**.
>
> Explanation: the whole distinction is about how naturally the data fit a stable table structure.

15. The sexy part of alternative data gets attention, but the legal and ethical warnings matter just as much. Web scraping can collect personal information, regulated information, or data used without clear consent.
16. Rules and best practices can differ across jurisdictions. **The exam takeaway is simple: "machine collected it" does not mean "safe to use."**
17. Before analysis even starts, Big Data creates practical problems.
18. The curriculum asks whether the dataset has selection bias, missing data, outliers, enough observations, and actual fitness for purpose. What is selection bias: distortion caused by how the observations were selected rather than by the real phenomenon. What are outliers: observations far away from the rest that can distort results.
19. Why this matters: a huge bad dataset is still a bad dataset.
20. Analysts usually have to source, clean, organize, and validate data before any clever model earns the right to exist.

21. Artificial intelligence sits above machine learning in the family tree. What is artificial intelligence: computer systems performing tasks that traditionally required human intelligence.
22. Why artificial intelligence is used: to recognize patterns, support decisions, and automate complex tasks at scale. Early artificial intelligence in finance often looked like expert systems using rule-based logic.
23. Later systems used stronger computing power and better networks to attack fraud detection, logistics, data mining, and financial analysis.
24. Machine learning is a more specific idea. What is machine learning: computer-based methods that learn patterns from data and then use those learned patterns on new cases.
25. The exam summary is wonderfully blunt: find the pattern, apply the pattern. Machine learning usually uses training data, validation data, and test data.
26. Training data teach the model. Validation data help tune it and check whether it is behaving sensibly.
27. Test data check whether the model actually generalizes to unseen cases.
28. Human judgment still matters because people choose the data, clean the data, define the question, and decide whether the output is nonsense.

29. Overfitting and underfitting are the classic model failures.
30. What is overfitting: the model learns the training data too closely and mistakes noise for signal.
31. What is underfitting: the model is too simple and misses real structure that is actually there.
32. Overfitting looks smart in the practice room and dumb in the real match.
33. Underfitting looks dumb in both places.
34. Some machine-learning models are also called black boxes.
35. What is a black box: a model where the path from input to output is hard to explain clearly.

> [!warning] MODEL TRAP
> Perfect performance on training data is not a victory parade.
>
> First ask whether the model learned the real pattern or just memorized noise.

36. Supervised learning means the model is trained with inputs and known outputs.
37. That makes it useful for prediction tasks like forecasting returns or classifying whether a borrower is likely to default.
38. Unsupervised learning means the model is not given labels and has to find structure by itself.
39. That makes it useful for clustering, grouping, and pattern discovery.
40. If a question says the algorithm is grouping firms into peer sets without preassigned labels, think unsupervised.
41. If it says the algorithm is trained on past inputs with known outcomes, think supervised.
42. Deep learning uses neural networks with many hidden layers and can be used in supervised or unsupervised settings.
43. Why hidden layers matter: they allow the model to build more complex representations from simpler patterns in stages.

> [!question] IDENTIFY THE MACHINE-LEARNING TYPE
> Problem: Identify the learning type in each case.
>
> 15. A model is trained on past borrower characteristics and known default outcomes.
> 16. A model groups listed companies into clusters without being told the sectors.
> 17. A neural-network system processes huge image and text datasets through many hidden layers.
>
> ---
>
> Solution:
>
> 18. Borrower characteristics plus known default outcomes = **supervised learning**.
> 19. Grouping unlabeled companies into clusters = **unsupervised learning**.
> 20. Neural network with many hidden layers = **deep learning**.
>
> Explanation: labels point to supervised learning, no labels point to unsupervised learning, and hidden-layer neural networks point to deep learning.

44. Data science is the broader craft that pulls these tools together. What is data science: the interdisciplinary use of computing, statistics, and related methods to extract useful information from data.
45. Data scientists try to convert raw data into actionable insight. In finance, that can mean prediction, monitoring, visualization, or decision support.
46. The source highlights five key data-processing methods: **capture, curation, storage, search, and transfer.**
47. Capture means collecting the data and converting them into usable form. Curation means cleaning the data and checking quality. Storage means how the data are recorded, archived, and organized.
48. Search means how the system retrieves specific information from huge datasets.
49. Transfer means moving the data from source or storage into the analytical tool.
50. Low latency matters most when the use case depends on fast reaction, like algorithmic trading. What is low latency: minimal delay in communication and processing.
51. Visualization is not decoration. It is a way of thinking. Traditional structured data often work fine with tables, line charts, and bar charts. Unstructured or highly multidimensional data may need heat maps, network graphs, tree diagrams, tag clouds, or mind maps.
52. What is a tag cloud: a word display where more frequent terms appear larger. What is a mind map: a visual layout showing how concepts connect rather than just how often they appear.

53. Text analytics and natural language processing matter a lot in investment work because finance produces endless language. Text analytics means using computer programs to analyze large text or voice datasets.
54. Natural language processing sits inside that world. What is natural language processing: the use of computing, artificial intelligence, and linguistics to analyze and interpret human language.
55. In practice, this means machines reading filings, transcripts, news, surveys, social posts, and policy speeches. It can support sentiment analysis, topic analysis, translation, speech recognition, compliance monitoring, and fraud detection.
56. In investment management, natural language processing can flag tone shifts in earnings calls, analyst reports, or central-bank communication before a human team fully processes them.

> [!example] WHEN THE CENTRAL BANK CHANGES ITS TONE BEFORE IT CHANGES THE RATE
> Markets do not always move because the policy rate changed. Sometimes they move because the language around inflation, growth, or "data dependence" shifted first. Natural language processing helps machines catch the whisper before the headline shout.

57. The curriculum also names common programming languages and database types used around data science. Python is widely used and approachable. R is especially strong in statistics and econometrics. Java is useful across operating systems and many internet applications. C and C++ matter when speed is critical, especially in algorithmic and high-frequency trading settings.
58. Excel VBA still shows up in automation-heavy workflows. On the database side, SQL fits structured rows-and-columns data. SQLite is a lightweight structured database often embedded in software. NoSQL is useful when data do not fit traditional structured tables.
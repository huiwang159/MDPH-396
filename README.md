# Background
This is a project with McGill University Health Centre that classifies Radiation Oncology Incident Reports according to the taxonomy of the Canadian National System for Incident Reporting. [This](https://www.authorea.com/users/222819/articles/277226-using-natural-language-processing-to-classify-incident-reports-in-radiation-oncology) is a link to the report.
# Abstract
## Purpose
Incident learning in radiotherapy may improve the quality of care by reducing the recurrence of incidents. Incident reports are often descriptions in free-text format, which makes it difficult to extract information efficiently and determine if a report is complete. Natural language processing (NLP) is a proven technique in extracting information from clinical texts and classifying safety reports, but the utility of NLP in classifying radiotherapy incident reports is untested. This project illustrates an NLP approach to classifying radiotherapy incident reports by the process step of incident occurrence, and determining if a report is complete.
## Methods
A preliminary analysis that consisted of tagging of parts-of-speech (POS)  and annotation with the Unified Medical Language System (UMLS) was conducted on 519 reports. The summary statistics of the preliminary analysis was used to compare fictitious reports deemed complete and reports of real incidents. Multinomial classification by the process step of incident occurrence was transformed into multiple binomial classifications by one-hot encoding. The reports were subsequently cleaned and vectorized into a bag of words, on which the naive binomial bayesian classifiers were trained and tested. Receiver-operating-characteristic (ROC) curves were then plotted to evaluate each binomial classifier.
## Results
The number of occurrence of several POS were statistically different in the fictitious and real reports, and the performance of the binary classifiers varied from poor to excellent with an average area under the curve (AUC) of 0.85.
## Conclusion
Determining if a report is complete requires domain knowledge outside the scope of statistical NLP. However, NLP can classify incidents by process step with fair performance, and demonstrates the potential to classify incidents by other data elements of the Canadian National System for Incident Reporting - Radiation Treatment (NSIR-RT).

![][Safer Radiotherapy.png]

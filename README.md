# The Generation of Synthetic Healthcare Data Using Deep Neural Networks

## Overview
- Master Thesis in Computational Engineering 
- Unversity of Stavanger - Spring 2022 
- Thesis was conducted in collaboration with SimulaMet center  
- Supervisors: Michael Alexander Riegler, Andrea Storås

## Abstract
High-quality tabular data is a crucial requirement for developing data-driven applications, especially healthcare-related ones, because most of the data nowadays
collected in this context is in tabular form. However, strict data protection laws introduced in Health Insurance Portability and Accountability (HIPAA) and General
Data Protection Regulation (GDPR) present many obstacles to accessing and doing scientific research on healthcare datasets to protect patients’ privacy and confidentiality.
Thus, synthetic data has become an ideal alternative for data scientists and healthcare professionals to circumvent such hurdles. Although many healthcare data
providers still use the classical de-identification and anonymization techniques for generating synthetic data, deep learning-based generative models such as Generative
Adversarial Networks (GANs) have shown a remarkable performance in generating tabular datasets with complex structures. Thus, this thesis examines the GANs’ potential and applicability within the healthcare industry, which often faces serious challenges with insufficient training data and patient records sensitivity. <br>
We investigate several state-of-the-art GAN-based models proposed for tabular synthetic data generation. Precisely, we assess the performance of TGAN, CTGAN, CTABGAN, and WGAN-GP models on healthcare datasets with different sizes, numbers of variables, column data types, feature distributions, and inter-variable correlations. Moreover, a comprehensive evaluation framework is defined to evaluate the quality of the synthetic records and the viability of each model in preserving the patients’ privacy. After training the selected models and generating synthetic datasets, we evaluate the strengths and weaknesses of each model based on the statistical similarity metrics, machine learning-based evaluation scores, and distance-based privacy metrics. <br>
The results indicate that the proposed models can generate datasets that maintain the statistical characteristics, model compatibility, and privacy of the original ones. Moreover, synthetic tabular healthcare datasets can be a viable option in many data-driven applications. However, there is still room for further improvements in designing a perfect architecture for generating synthetic tabular data. 



## Motivation and Main contributions
To see the motivations and main contributions of this work, please have a look at my master thesis, found at https://uis.brage.unit.no/uis-xmlui/handle/11250/3022990 



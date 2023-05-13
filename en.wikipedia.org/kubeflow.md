Kubeflow is an open-source platform for machine learning and MLOps on
Kubernetes introduced by Google. The different stages in a typical
machine learning lifecycle are represented with different software
components in Kubeflow, including model development (Kubeflow
Notebooks), model training (Kubeflow Pipelines, Kubeflow Training
Operator), model serving (KServe), and automated machine learning
(Katib). Each component of Kubeflow can be deployed separately, and it
is not a requirement to deploy every component. History The Kubeflow
project was first announced at KubeCon + CloudNativeCon North America
2017 by Google engineers David Aronchick, Jeremy Lewi, and Vishnu Kannan
to address a perceived lack of flexible options for building
production-ready machine learning systems. The project has also stated
it began as a way for Google to open-source how they ran TensorFlow
internally.The first release of Kubeflow (Kubeflow 0.1) was announced at
KubeCon + CloudNativeCon Europe 2018 with claims of having already
become among the top 2% of GitHub projects ever. Kubeflow 1.0 was
released in March 2020 via a public blog post announcing that many
Kubeflow components were graduating to a \"stable status\", indicating
they were now ready for production usage. Components Kubeflow Notebooks
for model development Machine learning models are developed in the
notebooks component called Kubeflow Notebooks. The component runs
web-based development environments inside a Kubernetes cluster, with
native support for Jupyter Notebook, Visual Studio Code, and RStudio.
Kubeflow Pipelines for model training Once developed, models are trained
in the Kubeflow Pipelines component. The component acts as a platform
for building and deploying portable, scalable machine learning workflows
based on Docker containers. Google Cloud Platform has adopted the
Kubeflow Pipelines DSL within its Vertex AI Pipelines product. Kubeflow
Training Operator for model training For certain machine learning models
and libraries, the Kubeflow Training Operator component provides
Kubernetes custom resources support. The component runs distributed or
non-distributed TensorFlow, PyTorch, Apache MXNet, XGBoost, and MPI
training jobs on Kubernetes. KServe for model serving The KServe
component (previously named KFServing) provides Kubernetes custom
resources for serving machine learning models on arbitrary frameworks
including TensorFlow, XGBoost, scikit-learn, PyTorch, and ONNX. KServe
was developed collaboratively by Google, IBM, Bloomberg, NVIDIA, and
Seldon. Publicly disclosed adopters of KServe include Bloomberg, Gojek,
and others. Katib for automated machine learning Lastly, Kubeflow
includes a component for automated training and development of machine
learning models, the Katib component. It is described as a
Kubernetes-native project and features hyperparameter tuning, early
stopping, and neural architecture search. Release timeline Notes
References External links Official website Kubeflow on GitHub

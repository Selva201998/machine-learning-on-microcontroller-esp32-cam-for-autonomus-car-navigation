# Project Overview

Moreover, a distinctive approach to this project involves a comparative analysis of the computational capabilities and performance between the micro-controller-based system and conventional computer setups. By undertaking this comparison, we aim to shed light on the practicality and feasibility of micro-controller technology for real-world navigation scenarios, thereby offering crucial insights into the potential of our hypothesis-driven approach.

## Hypotheses

1. **Hypothesis 1:** We hypothesize that the integration of machine learning algorithms, such as Convolutional Neural Networks (CNN) and Principal Component Analysis (PCA), with the ESP32 CAM micro-controller will enable real-time object recognition and obstacle avoidance, contributing to enhanced autonomous navigation capabilities.

2. **Hypothesis 2:** We posit that the optimization of machine learning models for the ESP32 CAM micro-controller, achieved through techniques like quantization and pruning, will result in a significant reduction in memory usage without compromising navigation accuracy.

3. **Hypothesis 3:** It is our hypothesis that the utilization of the ESP32 CAM micro-controller's low power consumption capabilities will lead to an energy-efficient autonomous vehicle system, making it suitable for prolonged operation in resource-constrained environments.

4. **Hypothesis 4:** We anticipate that the comparative analysis between micro-controller-based systems and traditional computers will reveal the ESP32 CAM microcontroller’s suitability for cost-effective and efficient autonomous navigation, potentially revolutionizing the landscape of autonomous vehicle technology.

## Project Objectives

### 1. Autonomous Car System with Micro-controller Camera (ESP32 CAM)
Develop a sophisticated autonomous car (Donkey Car) system that effectively employs a micro-controller camera, specifically the ESP32 CAM, for seamless visual perception and navigation.

### 2. Machine Learning Algorithm for Navigation
Design and implement an advanced machine learning algorithm that capitalizes on the processed visual data. This algorithm will drive navigation decisions to ensure optimal path planning for the autonomous vehicle.

### 3. Integration of DC Motor and Micro-controller
Effectively integrate the DC motor with the ESP32 CAM micro-controller to facilitate precise control over the car’s motions. This integration will enable the system to enact navigation decisions encompassing speed modulation, directional shifts, and steering adjustments.

### 4. Optimization of Computational Efficiency and Memory Usage
The overarching goal is to attain peak performance while abiding by the constraints intrinsic to micro-controller technology and establish a comparison point with conventional computer processing power.

## Project Scope

### 1. Machine Learning Algorithm Innovation
Designing the machine learning algorithm to process real-time visual inputs, such as images, and make navigation choices and perform decision-making processes and hardware control.

### 2. ESP32 Micro-controller Integration
The fusion of ESP32 CAM microcontroller with the motor controller for motor speed. Culminating in a comprehensive system that captures visual data, executes machine learning computations, and influences the vehicle’s movement.

### 3. Comparison of Machine Learning Approaches
Investigate different machine learning algorithms like Convolutional Neural Networks, MobileNetV2, and Principal Component Analysis. Find out the suitable for the micro-controller and implement it.

### 4. Optimization of Computational Efficiency
Optimize the machine learning algorithm compatible with the ESP32 CAM micro-controller using Edge Impulse.

### 5. Comparison with Conventional Computers
A unique aspect of this project involves comparing the computational capabilities and performance of the micro-controller-based systems with conventional computer setups. This comparison provides insights into the viability of microcontroller technology for real-world navigation scenarios.

## Methodology
\label{sec:Methodology}
\begin{figure}[ht]
    \centering
    \begin{tikzpicture}[node distance=2cm]
    
    % Define styles for nodes
    \tikzstyle{startstop} = [rectangle, rounded corners, minimum width=2.5cm, minimum height=1cm, text centered, draw=black, fill=red!30]
    \tikzstyle{process} = [rectangle, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=orange!30]
    \tikzstyle{arrow} = [thick,->,>=stealth]
    
    % Nodes
    \node (datacollection) [startstop] {Experimental Setup and Data Collection};
    \node (datasplit) [process, below of=datacollection] {Data Splitting (Training, Test)};
    \node (datapreprocessing) [process, below of=datasplit] {Data Preprocessing};
    \node (machinelearning) [process, below of=datapreprocessing] {Machine Learning Models};
    \node (edgeimpulse) [process, below of=machinelearning] {Optimize ML model and deploy into ESP32 micro-controller};
    \node (testmodel) [process, below of=edgeimpulse] {Test the Model};
    \node (end) [startstop, below of=testmodel] {End};
    
    % Arrows
    \draw [arrow] (datacollection) -- (datasplit);
    \draw [arrow] (datasplit) -- (datapreprocessing);
    \draw [arrow] (datapreprocessing) -- (machinelearning);
    \draw [arrow] (machinelearning) -- (edgeimpulse);
    \draw [arrow] (edgeimpulse) -- (testmodel);
    \draw [arrow] (testmodel) -- (end);
    
    \end{tikzpicture}
    \caption{Workflow Diagram}
    \label{fig:workflow}
\end{figure}


### Experimental Setup and Data Collection
In the initial phase of our project, we meticulously set up a controlled laboratory environment for data collection. This included carefully managing lighting conditions and camera angles to ensure the creation of a diverse and representative image dataset. The data collection process itself involved manual driving of the vehicle along a predefined path, exclusively utilizing the ESP32 camera module for image capture. This deliberate setup allowed us to gather data under consistent conditions, setting the stage for robust experimentation.

### Data Splitting (Training, Test)
To ensure the validity and generalization capabilities of our machine learning model, we adopted a rigorous data splitting strategy \cite{datasetsplitting}. This involved partitioning the collected dataset into three subsets: a training set, a validation set, and a test set. Specifically, 60% of the images were allocated for training, while 20% each were reserved for validation and testing. This balanced distribution aimed to minimize bias and enhance the model's ability to generalize to new data \cite{9530464}, \cite{DBLP:journals/corr/abs-2106-07597}.

### Data Preprocessing: Image Resizing
Prior to feeding images into the machine learning model, preprocessing steps are undertaken to ensure and enhance model performance. In the data preprocessing phase, we standardized the resolutions of our images, transitioning from the initial 112 x 84 pixels to a uniform 32 x 28 pixels to align with our model's requirements. Given the grayscale nature of our images, additional normalization or complex segmentation was deemed unnecessary. Our primary focus during preprocessing was distinguishing between the foreground (white strips) and background (black areas), as accurate vehicle navigation relied on identifying the white strips \cite{mi13020250}. Remarkably, our dataset inherently contained diverse image angles and rotations, rendering traditional data augmentation techniques, such as rotation and brightness adjustments, redundant for our project.

### CNN Architecture Design
Designing an optimal convolution neural network architecture is the main aim of the project's success. When designing a CNN architecture, it is important to carefully consider factors such as the number and arrangement of convolutional layers, pooling layers, and fully connected layers. The overall architecture should be designed to effectively capture both local and global features present in the input data, while also maintaining a balance between model complexity and computational efficiency. Additionally, it is crucial to conduct comparative evaluations of different architecture variants using aggregated performance metrics such as accuracy, model complexity, and computation efficiency. These metrics provide valuable insights into the effectiveness of design decisions and help determine the best architecture for a given task.

### Optimize ML model and Deployment into ESP32 micro-controller
The optimization and deployment of our machine learning model onto the ESP32 CAM microcontroller were streamlined through the utilization of the Edge Impulse platform. This platform played a pivotal role in converting the trained model into a resource-efficient format compatible with the microcontroller's computational capabilities and memory constraints. The process entailed generating optimized C++ code and seamlessly integrating it with the ESP32 CAM, enabling real-time predictions. Additionally, Edge Impulse simplified the integration with necessary libraries, effectively bridging the gap between the development and deployment phases of our machine learning model. The resulting optimized C++ code, along with the essential libraries, was seamlessly incorporated into the Arduino IDE for further development and deployment.

# Visual Odometry Part I: The First 30 Years and Fundamentals

Given the comprehensive details from the paper you provided, here are multiple summarizations highlighting different aspects of the discussed technologies and methods:

### General Overview of SFM, VO, and SLAM

1. **Structure from Motion (SFM)** is a technique aimed at reconstructing both the 3D structure of a scene and the camera poses from a set of images, which can be either sequentially ordered or unordered. The process involves an offline optimization known as bundle adjustment, which refines the final structure and camera poses but becomes computationally intensive with an increase in the number of images.

2. **Visual Odometry (VO)**, in contrast, is designed for estimating the 3D motion of the camera in real time and on a frame-by-frame basis. While it can employ bundle adjustment for local trajectory refinement, its primary focus is on the immediate estimation of camera movement.

3. **Simultaneous Localization and Mapping (SLAM)**, and specifically Visual SLAM (V-SLAM), seeks to achieve a global, consistent estimate of a robot's path and involves mapping the environment. This process is crucial for recognizing when the robot revisits an area (loop closure), which helps reduce drift in both the map and camera path.

### Specialized Techniques and Considerations

4. **Single Camera vs. Stereo Vision**: Using a single camera only provides bearing information, limiting motion recovery to a scale factor. Absolute scale can be established through direct measurements or integration with other sensors. This contrasts with stereo vision, which can provide more detailed spatial information.

5. **Local Optimization**: To minimize drift, especially in critical applications, local optimization techniques such as sliding window or windowed bundle adjustment are employed. These methods adjust the last few camera poses to ensure minimal error in the estimated trajectory.

6. **Path and Environment Mapping**: If only the camera path is of interest, a full V-SLAM method might be overkill. However, V-SLAM offers higher precision by enforcing additional constraints on the path, though it may not be as robust due to potential outliers in loop closure events.

7. **Motion Estimation**: The core of VO involves computing relative transformations between consecutive images to piece together the camera's full trajectory. This may be further refined through windowed-bundle adjustment for a more accurate local trajectory estimate.

8. **Feature-based Methods**: Preferred for their speed and accuracy, feature-based methods are predominant in VO implementations. They require robust feature matching across frames and assume camera calibration for motion estimation.

9. **2-D-to-2-D vs. 3-D-to-3-D Matching**: The paper discusses two approaches to establishing feature correspondences: 2-D-to-2-D, which works directly with image coordinates and is preferred in monocular setups to avoid point triangulation, and 3-D-to-3-D, which requires triangulating 3-D points, often using a stereo camera system.

### Key Mathematical Tools and Techniques

10. **The Essential Matrix**: In the 2-D-to-2-D approach, the essential matrix is computed from feature correspondences to extract rotation and translation information. This is crucial for motion estimation and requires proper scaling to address the absolute scale ambiguity present in monocular setups.

These summarizations encapsulate the core ideas and methodologies discussed in the paper, touching on the distinctions, applications, and specific techniques within SFM, VO, and SLAM frameworks.



# Comprehensive Summarization of Indoor Positioning Technologies and Challenges

1. **Prevalence of Wi-Fi in Indoor Positioning**: The paper highlights Wi-Fi as the predominant technology for indoor positioning, favored for its widespread infrastructure. Despite its popularity, Wi-Fi's effectiveness is hampered by signal attenuation and multipath effects caused by indoor environments, which lead to inaccuracies in location estimation.

2. **Camera-based Positioning Strategies**: Deploying cameras within infrastructure aims to maximize visual coverage for target location and tracking. On mobile devices, cameras strive to capture the largest possible area around the user to identify visually registered references, addressing the challenge of achieving comprehensive visibility in varied settings.

3. **Classification of Indoor Positioning Systems (IPS)**: IPS are categorized into self-positioning, where devices independently ascertain their locations; infrastructure positioning, relying on fixed environmental devices for location estimation; and self-directed infrastructure-assisted, where an external system calculates and relays positions back to users. This classification underscores the diverse approaches to indoor positioning, each with its own set of challenges and applications.

4. **Range-based vs. Range-free Methods**: The paper distinguishes between range-based methods, which derive geometric data (distance or angle) from wireless node signals, and range-free methods, dependent on connectivity or identifiable signal patterns. This division reflects the varying methodologies in IPS, highlighting the trade-offs between accuracy and system complexity.

5. **Time-based Location (ToF) Challenges**: Time of Flight (ToF) methods measure signal propagation time to estimate distances. However, their accuracy is significantly affected by indoor structures, layout variations, and synchronization issues between transmitting and receiving devices, illustrating the sensitivity of IPS accuracy to environmental factors.

6. **Advancements with Ultra-Wideband (UWB) Technology**: UWB technology is noted for improving range accuracy through the use of large bandwidths, enabling shorter pulse implementations that enhance time resolution and positioning estimates. This advancement represents a significant step forward in overcoming the limitations of traditional time-based location methods.

7. **Angle of Arrival (AoA) and Hardware Requirements**: AoA systems, which calculate the direction of an incoming signal, are not widely adopted for indoor positioning due to the necessity for additional hardware. This point underscores the balance between system capabilities and the practicality of deployment in real-world settings.

8. **Received Signal Strength Indicator (RSSI) Utilization**: RSSI-based location methods estimate distances using signal strength but suffer from low accuracy influenced by environmental factors like walls and human bodies. Despite these challenges, RSSI is attractive for its minimal infrastructure needs and the ability to operate without network connectivity, leveraging existing Wi-Fi networks.

9. **Bluetooth Low-Energy (BLE) Beacons for Indoor Positioning**: BLE beacons have gained popularity for indoor positioning due to their low cost, low power consumption, and widespread support by modern smartphones. This technology represents a growing trend towards more efficient and user-friendly IPS solutions.

10. **Magnetic Field-based Positioning and Its Limitations**: IPS based on magnetic fields measure variations to estimate positions but struggle with site individualization due to non-unique magnetic values. This limitation points to the challenges of achieving accurate and distinctive location identification within complex indoor environments.

11. **Error Growth and Environmental Influence**: The paper discusses how errors in position estimation can grow cubically over time due to accelerometer and gyroscope integration, though systems based on steps and headings show linear error growth. Additionally, the accuracy of magnetometer-based location estimation can be compromised by indoor ferromagnetic materials, highlighting the impact of environmental variables on IPS performance.

12. **Conclusion and Future Directions**: The detailed examination of various indoor positioning technologies reveals a landscape marked by a continuous search for balance between accuracy, system complexity, and environmental adaptability. The evolution of IPS technology is driven by the need to overcome inherent limitations posed by indoor environments, with ongoing research focusing on refining existing methodologies and exploring new approaches to enhance reliability and usability.



# Visual Odometry (VO) and SLAM

## Definition of Visual Odometry (VO)
- VO is the process of estimating the **ego-motion** of an agent (e.g., vehicle, human, robot) using the input from one or several cameras attached to it.

## Difference Between VO and SLAM
- **VO**:
  - Focuses on **local consistency**.
  - Aims to **incrementally estimate the path** of the camera/robot, pose after pose.
  - May involve **local optimization**.
- **SLAM** (Simultaneous Localization and Mapping):
  - Aims to achieve a **globally consistent estimate** of the camera/robot trajectory and map.

## Challenges in VO
- **System Errors**:
  - Errors accumulate due to incorrect step displacement segmentation and inaccurate stride estimation.
- **Scale Factor**:
  - VO typically provides the camera's motion up to a scale factor.
  - Direction and relative speed are measurable, but not the actual distance traveled.
  - **Depth information from 2D images is not absolute.**
  - However, visual odometry by itself typically provides the camera's motion up to a scale factor — it can tell you the direction and relative speed of the movement, but not the actual distance traveled. This is because the depth information from 2D images is not absolute; it's based on the apparent size of objects, which can change depending on their actual size and distance from the camera.

## Visual-Inertial Odometry (VIO) for Irregular Gait
- Traditional **step counting algorithms** fail with irregular gait, often seen with visually impaired people in unfamiliar environments.
- **VIO** replaces step counting and functions well despite irregular gait patterns.
- Combines visual feature tracking with data from the smartphone’s **inertial measurement unit (IMU)**.
- Estimates changes in smartphone’s **(X, Y, Z) location and 3D orientation** (roll, pitch, and yaw).
- Movement estimates are projected to the **2D map domain**, continuously estimating the user’s trajectory.

## Magnetic Data

### Using Bp Directly
- Collect magnetic field readings in all directions.
  - Increases training cost.
  - Reduces accuracy as the sample space becomes larger.
- Estimation of phone orientation can be error-prone.
  - Errors are amplified when transforming Bp to the earth coordinate system (Be).

### Using Magnitude B of Bp
- B is rotation invariant and stable.
- Reduces elements in each fingerprint from three to one.
  - May reduce uniqueness, increasing time for particle filter convergence.

### Extracting Horizontal (Bh) and Vertical (Bv) Components
- Utilizes the smartphone's gravity sensor to determine vertical direction.
- Constructs a new observation value (Bh,Bv) - termed HV fingerprint.
- HV fingerprint is more unique than magnitude fingerprint.
- **Challenges**:
  - Precision decreases with user movement.
  - Can introduce noise, leading to decreased precision or localization failure.

## Conclusion
- **VO and VIO** are critical in navigating and mapping for agents.
- **VO** deals with local motion estimation, while **SLAM** provides a global picture.
- **VIO** offers solutions for motion estimation in cases of irregular gait.
- **Observation techniques** need to balance between accuracy, training cost, and the uniqueness of location fingerprints.



# Particle Filtering Sampling & Distribution

![Screen Shot 2024-02-08 at 4.30.37 PM](/Users/renpeng/Library/Application Support/typora-user-images/Screen Shot 2024-02-08 at 4.30.37 PM.png)

https://stats.stackexchange.com/questions/229036/sampling-importance-resampling-why-resample











VO is the process of estimating the egomotion of an agent (e.g., vehicle, human, and robot) using only the input of a single or multiple cameras attached to it

The main dif- ference between VO and SLAM is that VO mainly focuses on local consistency and aims to incrementally estimate the path of the camera/robot pose after pose, and possibly performing local optimization. Whereas SLAM aims to obtain a globally consistent estimate of the camera/robot trajectory and map



System errors still quickly accumulate, because of incorrect step displacement segmentation and inaccurate stride estimation

However, visual odometry by itself typically provides the camera's motion up to a scale factor — it can tell you the direction and relative speed of the movement, but not the actual distance traveled. This is because the depth information from 2D images is not absolute; it's based on the apparent size of objects, which can change depending on their actual size and distance from the camera.

However, while the step counting algorithm works well for participants who walk with a regular gait, it is unreliable when the gait becomes irregular and halting – which is not unusual when visually impaired people explore unfamiliar surroundings. Accordingly, in our new approach we replaced step counting with visual-inertial odometry (VIO) [8], which functions well even if the user is walking with an irregular gait.

We accomplish this using VIO [8], which combines the tracking of visual features in the environment with data from the smartphone’s inertial measurement unit (IMU) to estimate changes in the smartphone’s (X, Y, Z) location and 3D orientation (roll, pitch and yaw) over time. These movement estimates are projected to the 2D map domain, so that the user’s trajectory on the map is estimated continuously over time.

*Using* Bp *directly as observation* z [4, 7, 11, 12]. One method is to collect the magnetic field readings of all direc- tions at any location, which not only increases the training cost rapidly, but also reduces the accuracy as the sample s- pace becomes larger. Alternatively, we can estimate phone orientation and transform Bp to the earth coordinate system Be. However, this is error-prone because orientation estima- tion usually contains errors and these errors will be amplified on Be.

*Using the magnitude* B *of* Bp *as observation* [11, 22]. B is a rotation invariant scalar quantity and quite stable. However, the elements in each fingerprint will drop from three to one, reducing the uniqueness of each fingerprint. In large indoor environments, the particle filter may need more time to con- verge to the right location.

*Extracting the horizontal component* Bh *and vertical compo- nent* Bv *of* Bp *as observation* [13]. The gravity sensor on smartphone provides us the direction of gravity (i.e., the ver- tical direction). We can extract both the vertical and horizon- tal components of Bp and construct a new observation value (Bh,Bv) (named HV fingerprint). Figure 7 shows the mag- netic field map of these two components in an indoor area. Obviously, it is more unique than the magnitude fingerprint, which will make the particle filter converge to the right lo- cation faster. This fingerprint model was mentioned in Ref [13], but there is no real-world magnetic fingerprinting based indoor localization system depends on it. That is because the gravity sensor reading is very precise when the user stands still. However, noise will be introduced when the user moves, resulting in decreasing in precision or even localization fail- ure.



The most used so far is Wi-Fi technology.

When applied to the infrastructure, the cameras are arranged to cover the largest visual field so that the targets can be located and tracked. When cameras are used on mobile devices, the objective is to cover the largest visible area around the user and visually identify information registered as a reference.

However, in the indoor environment, the accuracy of satellite-based positioning decreases markedly due to signal losses when colliding with building structures, which causes the effects of multiple paths and delays in information delivery, thus not meeting the requirements of a reliable service location

Indoor positioning systems classified based on their architecture can be divided into three classes:

(1) self-positioning, (2) infrastructure positioning, and (3) assisted by self-directed infrastructure.

In self-positioning architecture, devices determine their locations by themselves. In infrastructure

positioning architecture, device positions are estimated using the locations of devices launched in the

environment. In architecture assisted by self-directed infrastructure, an external system calculates the

Sensors 2020, 20, x FOR PEER REVIEW 6 of 36 position and sends it to the tracked user in response to a request.A more simplified way to classify network-based indoor positioning systems is to consider how information is obtained. In this classification model, there are two groups: (i) methods based on range and (ii) methods without range.

Range-based methods extract geometric information (distance or angle) from signals from

different wireless nodes and then combine the geometric constraints of each anchor to obtain the user’s

position [43]. Free-range methods are based on the connectivity information between nodes or the Sensors 2020, 20, x FOR PEER REVIEW 7 of 36

identification of signal resource patterns that depend on location [1].



Time-based location: Time-based location uses algorithms that measure the propagation time of a signal between the transmitter and the receiver [44]. This location model is also known as the time of offlight(ToF),andappliescalculationsthatindicatethedistance, 𝑑, betweentheuserandtheanchor node, as follows:

1. The use of time-based systems for indoor location has several limitations concerning its accuracy, caused by problems such as building structure, internal layout, and building location, which can cause the signals to be blocked

1. More recent works are based on UWB technology, which improves the accuracy of the range due to the large bandwidth used [11]. The use of a large bandwidth allows implementing shorter pulses that increase the resolution of time and the accuracy of positioning estimates by the ToF method.

1. Time-based location methods are susceptible to errors produced by clock inaccuracies, errors in time estimation, and a lack of synchronization between clocks [24]. For example, for a signal that travels at the speed of light, 1 μs of error corresponds to an approximate distance error of 300.00 m

In general, AoA systems are not widely used for the indoor location due to the need for additional hardware, such as sensor arrays or antennas



Unfortunately, the variability of the Wi-Fi channel, together with the signal attenuation caused by building structures such as walls, or other elements such as the human body itself, introduces errors into the distance estimation and makes RSSI-based location algorithms less accurate than time- or angle-based algorithms

RSSI: Location methods based on RSSI estimate the distance between the user and an anchor node using the strength of the received signal

A feature that facilitates the application of the model based on RSSI is that measurements can be obtained without the need to be part of the network. Besides, the cost of the system’s infrastructure is minimal if existing Wi-Fi networks are used. 

Thus, to estimate the distance between two points, it is necessary to model the environment with Wi-Fi devices using a signal propagation model.

As in the case of time-based location algorithms, the user’s position is estimated by combining distance information from various anchor nodes using a lateration method

Unfortunately, the accuracy provided by RSSI-based systems is low and is negatively affected by the distance between the transmitter and the receiver.





More recently, many authors have tried using Bluetooth Low-Energy

location estimate of a room. More recently, many authors have tried using Bluetooth Low-Energy

(BLE) beacons to identify and locate targets.

(BLE) beacons to identify and locate targets.

Bluetooth is a wireless communication technology that uses information that is digitally

Bluetooth is a wireless communication technology that uses information that is digitally

incorporated into radio frequency signals [58,61]. The standard was initially intended for the incorporated into radio frequency signals [58,61]. The standard was initially intended for the

exchange of data over short distances, with operating policies and protocol defined by the IEEE 802.15.1

exchange of data over short distances, with operating policies and protocol defined by the IEEE

standard

The widespread adoption of BLE occurred due to its availability (most modern smartphones support it), low cost, and extremely low power consumption. BLE devices allow fixed emitters to run on batteries for several months or even years

An IPS based on magnetic fields uses a magnetometer to measure variations in the magnetic field, which will be used to determine a person’s position [81]. The position estimation is commonly performed using methods such as digital printing. However, magnetic fields are less able to individualize the identification of a site, as the same value can be found in many different parts of a building unit. Typically, jobs and applications that use magnetic field-based fingerprints compare fingerprint strings instead of making point-to-point comparisons



In general, errors in estimating the position increase cubically with time due to the integration of the accelerometer and gyroscope signals

1. Fortunately, the error growth of the step and heading systems is linear over time, instead of cubic, as in the strapdown systems.
2. The user’s location is obtained by a magnetometer, which in indoor environments is influenced by ferromagnetic materials, and may result in a degraded position estimate
3. That is, the gyroscope produces high-precision measurements in the short term, and the magnetometer provides low-precision measurements that are stable over time

Therefore, this type of system cannot be applied for a long time without a correction strategy.


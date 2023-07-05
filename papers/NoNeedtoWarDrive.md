## No Need to War-Drive: Unsupervised Indoor Localization

The research paper discusses the concept of utilizing internal landmarks in buildings for accurate indoor positioning. The authors propose that these landmarks exist naturally in the environment and can serve as reference points for navigation within a building.

The paper highlights the challenges associated with achieving high precision in indoor positioning. While pervasive WiFi systems can provide precise location information, they require costly and meticulous calibration, which may need to be repeated as RF fingerprints change due to environmental factors.

The authors mention the use of urban dead-reckoning techniques, which involve computing the motion trajectory of a mobile phone using its accelerometer and compass. They also suggest partitioning indoor spaces into smaller sub-spaces using overheard WiFi access points.

The paper emphasizes the importance of confidence estimation in error measurements, allowing for appropriate weighting before combining location estimates. It mentions various signatures that can be used as landmarks, such as changes in GPS confidence when transitioning from outdoors to indoors or distinct accelerometer patterns associated with elevators.

The authors propose a system called UnLoc that utilizes sensor data from multiple phones and applies a clustering algorithm to discover organic landmarks (OLMs). These OLMs can be used to correct the user's path during offline analysis, improving location estimates.

The paper suggests that landmarks do not need to be unique throughout the entire building but should be unique within a WiFi sub-space to be considered valid. This enables localized recalibration, resulting in smaller localization errors.

The approach presented in the paper involves combining dead-reckoned estimates of a given landmark to compute its location. The authors argue that by considering random and independent dead-reckoning errors from sufficient measurements, the estimated mean will converge to the actual landmark location.

Furthermore, the paper mentions the development of a Finite State Machine (FSM) to recognize elevator motion patterns and the potential use of the gyroscope, which is believed to be insensitive to ambient magnetic fields.

Overall, the research paper proposes the use of internal landmarks as a means of achieving accurate indoor positioning without the need for extensive calibration, with UnLoc being the system that employs clustering and dead-reckoning techniques to discover and utilize these organic landmarks.

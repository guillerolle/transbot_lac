Idea para dotar de polivalencia al robot transbot:
- hacer la base móvil que lleve estanterías completas desde abajo
- hacer que las estanterías sean los módulos que provean la polivalencia 
	- estanterías puede ser pasivas (sólo soportan materiales)
	- pueden tener un brazo que se conecta a la base móvil
	- puede tener otras cosas, que se muevan de forma autónoma o integrada. 

![[transbot-stages.pdf]]

# Mechatronic Abilities

| ABILITY                       | Lvls | JS  | AMR | AMM |
| ----------------------------- | ---- | --- | --- | --- |
| CONFIGURABILITY               | 4    | 0   | 0   | 1   |
| PARAMETER ADAPTABILITY        | 4    | 0   | 1   | 1   |
| COMPONENT ADAPTABILITY        | 4    | 1   | 1   | 1   |
| TASK ADAPTABILITY             | 4    | 0   | 0   | 0   |
| HUMAN-ROBOT INTERACTION       | 8    | 1   | 4   | 6   |
| HRI-FEEDBACK                  | 8    | 2   | 2   | 2   |
| ROBOT-ROBOT INTERACTION       | 6    | 0   | 0   | 1   |
| HRI-SAFETY                    | 8    | 1   | 2   | 3   |
| SOCIAL HUMAN INTERACTION      | 7    | 0   | 0   | 0   |
| INTERACTION COMPLEXITY        | 4    | 0   | 0   | 0   |
| HUMAN INTERACTION MODALITY    | 6    | 0   | 0   | 1   |
| SOCIAL INTERACTION LEARNING   | 3    | 0   | 0   | 0   |
| DEPENDABILITY                 | 7    | 0   | 1   | 1   |
| UNCONSTRAINED MOTION          | 7    | 2   | 3   | 3   |
| CONSTRAINED MOTION            | 5    | 0   | 1   | 1   |
| GRASPING ABILITY              | 8    | 0   | 0   | 1   |
| HOLDING ABILITY               | 5    | 0   | 0   | 1   |
| HANDLING ABILITY              | 9    | 0   | 0   | 1   |
| PERCEPTION ABILITY            | 8    | 1   | 2   | 3   |
| TRACKING ABILITY              | 6    | 0   | 3   | 3   |
| OBJECT RECOGNITION            | 14   | 0   | 0   | 0   |
| SCENE PERCEPTION              | 6    | 0   | 2   | 2   |
| SELF-LOCALISATION             | 7    | 1   | 2   | 4   |
| DECISIONAL AUTONOMY           | 11   | 0   | 0   | 0   |
| ACTION ABILITY                | 9    | 0   | 3   | 3   |
| INTERPRETIVE ABILITY          | 9    | 0   | 0   | 0   |
| ENVISIONING ABILITY           | 8    | 0   | 1   | 2   |
| ACQUIRED KNOWLEDGE (LEARNING) | 15   | 0   | 0   | 0   |
| REASONING                     | 8    | 0   | 0   | 1   |
| OBJECT INTERACTION            | 7    | 0   | 0   | 1   |
| HUMAN INTERACTION             | 7    | 0   | 1   | 1   |

![[Pasted image 20260819122731.png]]


## JOYSTICK

### Abilities
 - **Human-Robot Interaction Feedback**
	- **Level 1** *Visual feedback* #required
		- "The user is able to assess the state of the robot by direct observation. The robot system does not provide any means of feeding back information to the user."
	- **Reason**
		- El operario debe ver al robot para controlarlo. Esto es lo estrictamente necesario. Normalmente va a tener una pantalla en algún lado.
	- **Technologies**
- **Human-Robot Interaction Safety**
	- **Level 1** *Basic safety* #required
		- "The robot operates with a basic level of safety appropriate to the task. Maintaining safe operation may depend on the operator being able to stop operation or continuously enable the operating cycle. The maintenance of this level of safety does not depend on software."
	- **Reason**
		- Botón de parada de emergencia que detenga al sistema de forma segura en el robot
		- Switch "hombre muerto" en el joystick: un botón debe estar presionado para que pueda accionarse.
	- **Technologies**
		- Human-Machine Interface
		- Sensing & Perception
		- Cognition
		- Human-Robot Collaboration
		- Communications
- **Unconstrained Motion**
	- **Level 2** *Pre-defined closed loop motion* #required
		- "Each motion controlled to satisfy position/speed goals within an error bound (e.g. hold position against forces below motive force; accuracy in environment depends on other abilities like perception)"
	- Motivo:
		- Lazo cerrado de velocidad para comando por joystick
	- **Technologies**
		- Mechanical Systems
		- Sensing & Perception
		- Actuation
		- Planning & Control
		- Localisation & Mapping
		- Materials
- **Perception Ability**
	- **Level 1** *Direct Single and Multi-parameter sensing* #required
		- "A robot uses sensors that provide a single, or multiple parameter output directly., for example a distance sensor, or a contact sensor. The robot utilises these outputs to directly alter behaviour within an operating cycle."
	- **Reason**
		- Detección autómatica de obstáculos y parada de emergencia automática (ojo, es una Ability diferente a la indicada en HRI-Safety).
	- **Technologies**
		- Sensing & Perception
		- Cognition

### Technologies
- Human-Machine Interface
- Sensing & Perception
- Cognition
- Human-Robot Collaboration
- Communications
- Mechanical Systems
- Actuation
- Planning & Control
- Localisation & Mapping
- Materials

## JOYSTICK -> AMR
### Abilities
- **Component Adaptability**
	- **Level 1** *Recognition of the need for adaptation*
		- "The system recognizes the need for component adaptation. For example a visual navigation system detects inconsistencies between its visual and ego motion. The system identifies the problem and the failing components but does not do anything to correct the problem."
	- Motivo:
		- Identificación de problemas de auto-localización. Aunque sea controlado por joystick, esto es necesario para etapas con mayor autonomía
	- **Technologies**
		- Learning & Adaptation
		- Sensing & Perception
		- Cognition
- **Human-Robot Interaction Feedback**
	- **Level 2** *Vision data feedback* 
		- "The system feedbacks visual information about the state of the operating environment around the robot based on data captured locally at the robot. The user must interpret this visual imagery to assess the state of the robot or its environment."
	- Motivo:
		- Una simple pantalla que muestre información del robot. Necesario para monitorear al sistema en etapas subsiguientes
	- **Technologies**
		- Human-Machine Interface
		- Sensing & Perception
		- Cognition
		- Human-Robot Collaboration
		- Communications
- **Self-localisation**
	- **Level 1** *Actuator position* 
		- "The robot knows where its own mechanical structures are because of an assessment of the position of each of its actuators. For example a platform can assess its own position based on the amount its wheels have turned."
	- **Reason**
		- Autolocalización por odometría
	- **Technologies**
		- Sensing & Perception
		- Cognition

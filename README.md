# UeStateMachineHandling
state machine implementation to handle UE state in 5G core

A)Registeration Management state of UE in 5G core as per standard:

3gpp standard ETSI TS 123 501 V17.5.0 (2022-07)  under section section 5.3.1 Registration and Connection Management :

5.3.2.2.1 5GS Registration Management states defines 
Two RM states are used in the UE and the AMF that reflect the registration status of the UE 
RM-DEREGISTERED.
RM-REGISTERED. 

In the RM-DEREGISTERED state, the UE state in core :
  a)remain in RM-DEREGISTERED state if receiving a Registration Reject upon Initial Registration
  b)enter RM-REGISTERED state upon receiving a Registration Accept

In the RM-REGISTERED state, 
   a)enter RM-DEREGISTERED state when receiving a Registration Reject message or a Deregistration message.
   b)RM-DEREGISTERED state for the UE after Implicit Deregistration



B)Connection Management state of UE in 5g core:

As per 3gpp standard ETSI TS 123 501 V17.5.0 (2022-07) 5.3.3.2 5GS Connection Management states section

Two CM states are used to reflect the NAS signalling Connection of the UE with the AMF: 
a) CM-IDLE
b) CM-CONNECTED 





   



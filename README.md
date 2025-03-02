# UeStateMachineHandling
state machine implementation to handle UE state in 5G core

3gpp standard 23.501 version 17.5 under section section 5.3.1 Registration and Connection Management :

5.3.2.2.1 5GS Registration Management states defines 
Two RM states are used in the UE and the AMF that reflect the registration status of the UE 
RM-DEREGISTERED.
RM-REGISTERED. 

In the RM-DEREGISTERED state, the UE shall:
  a)attempt to register using the Initial Registration procedure
  b)remain in RM-DEREGISTERED state if receiving a Registration Reject upon Initial Registration
  c)enter RM-REGISTERED state upon receiving a Registration Accept

In the RM-REGISTERED state, 
   a)Mobility Registration Update 
   b)Periodic Registration Update procedure 
   c)perform Deregistration procedure 
   d)enter RM-DEREGISTERED state when receiving a Registration Reject message or a Deregistration message.
   e)RM-DEREGISTERED state for the UE after Implicit Deregistration

   



   

The Registration Management is used to register or deregister a UE/user with the network, and establish the user context in the network. The Connection Management is used to establish and release the signalling connection between the UE and the AMF.

registration update:
Periodic Registration Update
Mobility Registration Update

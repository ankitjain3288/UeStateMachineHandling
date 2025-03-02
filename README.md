# UeStateMachineHandling
state machine implementation to handle UE state in 5G core

A)Registeration Management state of UE in 5G core as per standard:

3gpp standard ETSI TS 123 501 V17.5.0 (2022-07)  under section section 5.3.1 Registration and Connection Management :

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



B)Connection Management state of UE in 5g core:

As per 3gpp standard ETSI TS 123 501 V17.5.0 (2022-07) 5.3.3.2 5GS Connection Management states section

Two CM states are used to reflect the NAS signalling Connection of the UE with the AMF: 
a) CM-IDLE
b) CM-CONNECTED 

There are no AN signalling connection, N2 connection and N3 connections for the UE in the CM-IDLE state. 
Event expected when UE is in CM-IDLE state and in RM-REGISTERED :
 a) Service Request
 b) Registration Request
 c) Deregistration Request
 
  ue should move from CM-IDLE to CM-CONNECTED state for the UE whenever an N2 connection is established

In the CM-CONNECTED state, the UE shall: 
  
 - enter CM-IDLE state whenever the AN signalling connection is released
 - enter CM-IDLE state for the UE upon completion of the AN Release procedure



   



################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap, sys, thread, time
import numpy as np

class SampleListener(Leap.Listener):
    dataset = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],"float32")
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        time.sleep(0.3)
        # Get the most recent frame and report some basic information
        frame = controller.frame()

       # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
        #      frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))
        left=0
        right=0
        for pointable in frame.pointables:
            direction = pointable.direction

            handType = "Left hand" if pointable.hand.is_left else "Right hand"


            if handType=="Left hand" and left%5==0:
                thumb = direction[0] * Leap.RAD_TO_DEG
                dataset[3]=thumb
                thumb2 = direction[1] * Leap.RAD_TO_DEG
                dataset[4]=thumb2
                thumb3 = direction[2] * Leap.RAD_TO_DEG
                dataset[5]=thumb3
                left+=1
            elif handType=="Left hand" and left%5==1:
                Index = direction[0] * Leap.RAD_TO_DEG
                dataset[6] = Index
                Index2 = direction[1] * Leap.RAD_TO_DEG
                dataset[7] = Index2
                Index3 = direction[2] * Leap.RAD_TO_DEG
                dataset[8] = Index3
                left += 1
            elif handType=="Left hand" and left%5==2:
                Middle = direction[0] * Leap.RAD_TO_DEG
                dataset[9] = Middle
                Middle2 = direction[1] * Leap.RAD_TO_DEG
                dataset[10] = Middle2
                Middle3 = direction[2] * Leap.RAD_TO_DEG
                dataset[11] = Middle3
                left += 1
            elif handType=="Left hand" and left%5==3:
                Ring = direction[0] * Leap.RAD_TO_DEG
                dataset[12] = Ring
                Ring2 = direction[1] * Leap.RAD_TO_DEG
                dataset[13] = Ring2
                Ring3 = direction[2] * Leap.RAD_TO_DEG
                dataset[14] = Ring3
                left += 1
            elif handType=="Left hand" and left%5==4:
                Pinky = direction[0] * Leap.RAD_TO_DEG
                dataset[15] = Pinky
                Pinky2 = direction[1] * Leap.RAD_TO_DEG
                dataset[16] = Pinky2
                Pinky3 = direction[2] * Leap.RAD_TO_DEG
                dataset[17] = Pinky3
                left += 1
            if handType=="Right hand" and right%5==0:
                thumb = direction[0] * Leap.RAD_TO_DEG
                dataset[18]=thumb
                thumb2 = direction[1] * Leap.RAD_TO_DEG
                dataset[19]=thumb2
                thumb3 = direction[2] * Leap.RAD_TO_DEG
                dataset[20]=thumb3
                right+=1
            elif handType=="Right hand" and right%5==1:
                Index = direction[0] * Leap.RAD_TO_DEG
                dataset[21] = Index
                Index2 = direction[1] * Leap.RAD_TO_DEG
                dataset[22] = Index2
                Index3 = direction[2] * Leap.RAD_TO_DEG
                dataset[23] = Index3
                right += 1
            elif handType=="Right hand" and right%5==2:
                Middle = direction[0] * Leap.RAD_TO_DEG
                dataset[24] = Middle
                Middle2 = direction[1] * Leap.RAD_TO_DEG
                dataset[25] = Middle2
                Middle3 = direction[2] * Leap.RAD_TO_DEG
                dataset[26] = Middle3
                right += 1
            elif handType=="Right hand" and right%5==3:
                Ring = direction[0] * Leap.RAD_TO_DEG
                dataset[27] = Ring
                Ring2 = direction[1] * Leap.RAD_TO_DEG
                dataset[28] = Ring2
                Ring3 = direction[2] * Leap.RAD_TO_DEG
                dataset[29] = Ring3
                right += 1
            elif handType=="Right hand" and right%5==4:
                Pinky = direction[0] * Leap.RAD_TO_DEG
                dataset[30] = Pinky
                Pinky2 = direction[1] * Leap.RAD_TO_DEG
                dataset[31] = Pinky2
                Pinky3 = direction[2] * Leap.RAD_TO_DEG
                dataset[32] = Pinky3
                right += 1

        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            #print "  %s, id %d, position: %s" % (
            #    handType, hand.id, hand.palm_position)



            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
           # print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
           #     direction.pitch * Leap.RAD_TO_DEG,
            #    normal.roll * Leap.RAD_TO_DEG,
           #     direction.yaw * Leap.RAD_TO_DEG)
            if handType == "Left hand":
                pitch = direction.pitch * Leap.RAD_TO_DEG
                dataset[0] = pitch
                roll = normal.roll * Leap.RAD_TO_DEG
                dataset[1] = roll
                yaw = direction.yaw * Leap.RAD_TO_DEG
                dataset[2] = yaw
            elif handType == "Right hand":
                pitch = direction.pitch * Leap.RAD_TO_DEG
                dataset[33] = pitch
                roll = normal.roll * Leap.RAD_TO_DEG
                dataset[34] = roll
                yaw = direction.yaw * Leap.RAD_TO_DEG
                dataset[35] = yaw
            # Get arm bone
            arm = hand.arm
          #  print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
           #     arm.direction,
           #     arm.wrist_position,
           #     arm.elbow_position)
            print np.array2string(dataset, separator=', ')+','



def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
            sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    dataset = np.array(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "float32")
    main()

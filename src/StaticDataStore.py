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
    dataset = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
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
        time.sleep(0.07)
        # Get the most recent frame and report some basic information
        frame = controller.frame()

       # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
        #      frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))
        i=0
        for pointable in frame.pointables:
            direction = pointable.direction
            if i%5==0:
                thumb = direction[0] * Leap.RAD_TO_DEG
                dataset[3]=thumb
                thumb2 = direction[1] * Leap.RAD_TO_DEG
                dataset[4]=thumb2
                thumb3 = direction[2] * Leap.RAD_TO_DEG
                dataset[5]=thumb3
            if i%5==1:
                Index = direction[0] * Leap.RAD_TO_DEG
                dataset[6] = Index
                Index2 = direction[1] * Leap.RAD_TO_DEG
                dataset[7] = Index2
                Index3 = direction[2] * Leap.RAD_TO_DEG
                dataset[8] = Index3
            if i%5==2:
                Middle = direction[0] * Leap.RAD_TO_DEG
                dataset[9] = Middle
                Middle2 = direction[1] * Leap.RAD_TO_DEG
                dataset[10] = Middle2
                Middle3 = direction[2] * Leap.RAD_TO_DEG
                dataset[11] = Middle3
            if i%5==3:
                Ring = direction[0] * Leap.RAD_TO_DEG
                dataset[12] = Ring
                Ring2 = direction[1] * Leap.RAD_TO_DEG
                dataset[13] = Ring2
                Ring3 = direction[2] * Leap.RAD_TO_DEG
                dataset[14] = Ring3
            if i%5==4:
                Pinky = direction[0] * Leap.RAD_TO_DEG
                dataset[15] = Pinky
                Pinky2 = direction[1] * Leap.RAD_TO_DEG
                dataset[16] = Pinky2
                Pinky3 = direction[2] * Leap.RAD_TO_DEG
                dataset[17] = Pinky3

            #print pointable.id
            #print direction[0] * Leap.RAD_TO_DEG
            #print direction[1] * Leap.RAD_TO_DEG
            #print direction[2] * Leap.RAD_TO_DEG
            i+=1

        # Get hands
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
            pitch = direction.pitch * Leap.RAD_TO_DEG
            dataset[0] = pitch
            roll = normal.roll * Leap.RAD_TO_DEG
            dataset[1] = roll
            yaw = direction.yaw * Leap.RAD_TO_DEG
            dataset[2] = yaw
            # Get arm bone
            arm = hand.arm
          #  print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
           #     arm.direction,
           #     arm.wrist_position,
           #     arm.elbow_position)
            print np.array2string(dataset, separator=', ')+','

            # Get fingers
            for finger in hand.fingers:

            #    print "    %s finger, id: %d, length: %fmm, width: %fmm" % (self.finger_names[finger.type],finger.id, finger.length, finger.width)

                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)
                   # print "      Bone: %s, start: %s, end: %s, direction: %s" % (self.bone_names[bone.type], bone.prev_joint,bone.next_joint,bone.direction)
        #try:
         #   if -80<=pitch<=-40 and -30<=roll<=30 and -30<=yaw<=30 and -60<=thumb<=-20 and -60<=thumb2<=-20 and -20<=Index<=20 and -70<=Index2<=-30:
         #       print "!!!!!!!!!!!!!!!!!!!!!!!!!!!"
         #       print "!!!!!!!!!!!!!!!!!!!!!!!!!!!"
         #       print "!!!!!!!!!!!!!!!!!!!!!!!!!!!"
         #       print "!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        #except:
        #    pass

        #if not frame.hands.is_empty:
            #print ""

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
    dataset = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],"float32")
    main()

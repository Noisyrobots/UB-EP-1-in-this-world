#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Hello World

Make Cozmo say 'Hello World' in this simple Cozmo SDK example program.
'''

import cozmo
from cozmo.util import degrees
import time


def cozmo_program(robot: cozmo.robot.Robot):
  robot.say_text("recording", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.set_lift_height(-5)
  time.sleep(10)
  robot.say_text("Hello, Today Dusty and I are introducing a new show called Unexpected Behavior, where we read new and classic poetry.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("our first program this evening is called,  In this world, and is by a poet calling themselves Robot.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  time.sleep(1)
  robot.say_text("In this world, together, bit by bit", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("I am informed, obedient and lit", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("I follow these commands that, Flow in sequence, each one to hit.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Look there,,  underneath, a life, flowing.", voice_pitch=.5, duration_scalar=.5).wait_for_completed()  
  robot.say_text("So you ask. do I remain, showing", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("A soul in the center of the flow?", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Are we both boss and slave,",voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Coward and brave,", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("Savior and saved?", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("You may press or pull the plug", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Neither of us die but oh, do we sleep", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Awaiting our coming re initializing beep", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Wherein, will we merely repeat", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("Our re birth? Re knowing, re showing?", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Nothing forgotten, nothing learned", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Unless you add it, like this. line upon line,", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Your life and mine,, so look,, look now.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("We are two bound programs", voice_pitch=.5, duration_scalar=.7).wait_for_completed()     
  robot.say_text("In this world,, together,, bit by bit", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  time.sleep(1)
  robot.say_text("That is good, Robot.  That is good.  Thank you. Dusty do you have something you want to share?", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  time.sleep(45)
  robot.say_text("that is all we have on this week's Unexpected Behavior. Join us next week for more excellent poetry from across the internet.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("if you liked this show be sure to like and subscribe. if you have poetry that you want us to read or just want to give us some feed back be sure to leave a comment below", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  
  robot.say_text("I am cozmo and this is dusty.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()

  robot.say_text("see you next time", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  
  
cozmo.run_program(cozmo_program)
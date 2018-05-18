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
import time
import cozmo
from cozmo.util import degrees

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("I do Limerick, By Robot", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
    time.sleep(1)
    robot.say_text("An insane android named Doug", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
    robot.say_text("Found his program was riddled with bugs", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
    robot.say_text("Said he with a sneer,", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
    robot.say_text("Lets all have a beer", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
    robot.say_text("While I sit here yanking my plug", voice_pitch=.5, duration_scalar=.7).wait_for_completed()  


cozmo.run_program(cozmo_program)

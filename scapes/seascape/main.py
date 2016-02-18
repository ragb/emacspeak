import random
from boopak.package import *
from boodle import agent
from boodle import builtin

play = bimport('org.boodler.play')


water = bimport('org.boodler.old.water')

wavesounds = [
    water.waves_lapping, water.waves_light, water.waves_rough,
    water.waves_floopy, water.water_rushing, water.water_pouring,
    water.water_rapids]


class SurfWaves(agent.Agent):
    """Orchestrate wave agents SurfWaveSounds and SurfBackgroundWaves"""

    def run(self):
        for i in range(12):
            ag = SurfBackgroundWaves()
            self.sched_agent(ag)
        for i in range(16):
            ag = SurfWaveSounds()
            self.sched_agent(ag)


class SurfWaveSounds(agent.Agent):

    def run(self):
        ag = play.IntermittentSoundsList(
            mindelay=1.0, maxdelay=15.0,
            minpitch=0.2, maxpitch=1.0,
            minvol=0.02, maxvol=0.1,
            maxpan=1.5, sounds=wavesounds)
        self.sched_agent(ag)


class SurfBackgroundWaves(agent.Agent):

    def run(self):
        p = random.uniform(0.2, 1.0)
        v = random.uniform(0.01, 0.1)
        d = random.uniform(0.3, 5.0)
        pan = random.uniform(-1.5, 1.5)
        dur = self.sched_note_pan(water.waves_light, pan, pitch=p, volume=v)
        self.resched(dur * d)

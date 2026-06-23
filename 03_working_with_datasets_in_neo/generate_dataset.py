from pathlib import Path

import neo
import numpy as np
import quantities as pq

rng = np.random.default_rng(0)

# A 96-channel LFP-like signal sampled at 1 kHz for 10 s.
lfp = neo.AnalogSignal(rng.normal(size=(10000, 96)), units='uV',
                       sampling_rate=1000*pq.Hz, t_start=0*pq.s,
                       name='LFP')
lfp.array_annotate(channel_names=np.array([f'chan{i+1}' for i in range(96)]))

# A smaller 6-channel signal sampled at 30 kHz for 10 s.
hires = neo.AnalogSignal(rng.normal(size=(300000, 6)), units='uV',
                         sampling_rate=30000*pq.Hz, t_start=0*pq.s,
                         name='Subsample unprocessed signal')
hires.array_annotate(channel_names=np.array([f'ainp{i+1}' for i in range(6)]))

# A handful of spike trains, each labelled as single-unit, multi-unit or noise.
unit_types = ['sua', 'mua', 'noise', 'sua', 'mua', 'sua', 'noise', 'sua']
spiketrains = []
for i, unit_type in enumerate(unit_types):
    times = np.sort(rng.uniform(0, 10, size=rng.integers(50, 150)))
    st = neo.SpikeTrain(times*pq.s, t_start=0*pq.s, t_stop=10*pq.s, name=f'unit {i}')
    st.annotate(unit_type=unit_type)
    spiketrains.append(st)

# Trial-start events, alternating correct and error, every 3 s.
ts_times = np.arange(1, 10, 3) * pq.s
performance = np.array(['correct_trial' if i % 2 == 0 else 'error_trial'
                        for i in range(len(ts_times))])
events = neo.Event(ts_times, labels=np.array(['TS-ON'] * len(ts_times)),
                   name='TrialEvents')
events.array_annotate(performance_in_trial_str=performance)

# Assemble everything into a Block with one Segment.
segment = neo.Segment(name='recording')
segment.analogsignals.extend([lfp, hires])
segment.spiketrains.extend(spiketrains)
segment.events.append(events)
block = neo.Block(name='dataset')
block.segments.append(segment)

# Write the block to a NIX file that the notebook reads back in.
data_dir = Path(__file__).parent / 'data'
data_dir.mkdir(exist_ok=True)
out_path = data_dir / 'dataset.nix'
out_path.unlink(missing_ok=True)
with neo.NixIO(str(out_path), mode='ow') as io:
    io.write_block(block)
print(f'Wrote dataset to {out_path}')
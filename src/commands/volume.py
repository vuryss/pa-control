import click
import pulsectl


@click.group('volume')
def volume():
    pass


@volume.command('incr')
def volume_increase():
    pulse = pulsectl.Pulse('pa-control-custom')

    for sink in pulse.sink_list():
        min_value = round(round(min(sink.volume.values), 2) + 0.05, 2)
        min_value = min(1, min_value)
        pulse.volume_set_all_chans(sink, min_value)


@volume.command('decr')
def volume_decrease():
    pulse = pulsectl.Pulse('pa-control-custom')

    for sink in pulse.sink_list():
        min_value = round(round(min(sink.volume.values), 2) - 0.05, 2)
        min_value = max(0, min_value)
        pulse.volume_set_all_chans(sink, min_value)


@volume.command('mute')
def volume_decrease():
    pulse = pulsectl.Pulse('pa-control-custom')
    mute = False

    for sink in pulse.sink_list():
        if sink.mute == 0:
            mute = True

    for sink in pulse.sink_list():
        pulse.mute(sink, mute)

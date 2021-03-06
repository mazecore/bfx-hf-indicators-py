from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
from math import isfinite

class EMAVolume(Indicator):
  def __init__(self, args = []):
    [ period ] = args

    self._ema = EMA([period])

    super().__init__({
      'args': args,
      'id': 'emavol',
      'name': 'EMA Vol(%f)' % period,
      'seed_period': period,
      'data_type': 'candle',
      'data_key': '*'
    })

  def reset(self):
    super().reset()
    self._ema.reset()

  def update(self, candle):
    self._ema.update(candle['vol'])
    ema = self._ema.v()

    if isfinite(ema):
      super().update(ema)

    return self.v()

  def add(self, candle):
    self._ema.add(candle['vol'])
    ema = self._ema.v()

    if isfinite(ema):
      super().add(ema)

    return self.v()

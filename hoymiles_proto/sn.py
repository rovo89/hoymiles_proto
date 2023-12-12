class SN:
  _CHARS32 = '0123456789ABCDEFGHJKLMNPRSTUVWXY'

  def __init__(self, sn) -> None:
    self._int = self._str = self._str_alpha = None
    if isinstance(sn, int):
      self._int = sn
    elif len(sn) == 12:
      self._str = sn
    elif len(sn) == 9:
      self._str_alpha = sn

  @property
  def int(self):
    if self._int is None:
      if self._str is not None:
        self._int = int(self._str, 16)
      else:
        self._int = 0
        for i in range(0, 9):
          pos = self._CHARS32.find(self._str_alpha[i])
          shift = 42 - 5 * i - (0 if i <= 2 else 2)
          self._int |= pos << shift
    return self._int

  @property
  def str(self):
    if self._str is None:
      self._str = format(self.int, 'X')
    return self._str

  @property
  def str_alpha(self):
    if self._str_alpha is None:
      self._str_alpha = ''
      int = self.int
      for i in range(0, 9):
        shift = 42 - 5 * i - (0 if i <= 2 else 2)
        self._str_alpha += self._CHARS32[(int >> shift) & 31]
    return self._str_alpha

  def __str__(self) -> str:
    if self._str is not None:
      return self._str
    elif self._str_alpha is not None:
      return self._str_alpha
    else:
      int = self.int
      if int >= 0x2400_0000_0000 and int < 0x3800_0000_0000:
        return self.str_alpha
      else:
        return self.str

  def __int__(self) -> int:
    return self.int

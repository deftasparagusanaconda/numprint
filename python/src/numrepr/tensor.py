def tensor(thing) -> str:
	if hasattr(thing, '__iter__') and not isinstance(thing, (str, bytes)):
		return '[' + ','.join(tensor(x,) for x in thing) + ']'
	return str(thing)

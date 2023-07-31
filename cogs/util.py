import datetime

## Useful functions to call in cogs ##

## Change timedelta.total_seconds() to readable time ##
def HumanizeDuration(duration):
	seconds = int(duration)
	num = [0, 0, 0, 0, 0, 0]
	typ = [' year', ' month', ' week', ' day', ' hour', ' minute', ' second']
	i = 0
	message = ''

	while seconds >= 31556926:
		num[0] += 1
		seconds -= 31556926
	while seconds >= 2629743:
		num[1] += 1
		seconds -= 2629743
	while seconds >= 604800:
		num[2] += 1
		seconds -= 604800
	while seconds >= 86400:
		num[3] += 1
		seconds -= 86400
	while seconds >= 3600:
		num[4] += 1
		seconds -= 3600
	while seconds >= 60:
		num[5] += 1
		seconds -= 60
	num.append(seconds)

	for n in num:
		if n > 1:
			typ[i] += 's'
		i += 1
	i = 0
	for n in num:
		if not n == 0:
			message += str(num[i])
			message += typ[i]
			message += ', '
		i += 1

	return message.strip(', ')

from seasons import calculate_age_in_minutes
from datetime import date


def test_calculate():
	assert calculate_age_in_minutes(date(2021, 12, 31)) == (
		(date.today() - date(2021, 12, 31)).days * 24 * 60 + \
		(date.today() - date(2021, 12, 31)).seconds // 60
	)
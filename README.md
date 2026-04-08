# HOW TO USE
- open folder in terminal
- type in "make" (no quotations, just the word) and enter
- you don't have to run python3 __init__.py --> "make" does it for you
- if it doesn't work, you might need to configure the venv and pip install (see notes on venv)

## USAGE EXAMPLE
Note: app is case-sensitive and is not dummy-proof
### General: uses full dataset
- Limit: General
- Specification: content_category
- Metric: reach

### has a limit
- Limit: content_category/Technology
- Specification: hashtags_count
- Metric: reach

# notes on venv
* python3 -m venv .venv
* source .venv/bin/activate
* pip install flask pandas numpy plotly

* in Makefile: https://stackoverflow.com/questions/33839018/activate-virtualenv-in-makefile#comment93719776_33839284 

====================================
# PART ONE : DATA EXPLORATION 
## SPECIFICATIONS
- account_type (brand/creator)
- media_type (reel/image/carousel)
- content_category (Technology/Fitness/etc)
- traffic_source (Home Feed/Hashags/etc)
- has_call_to_action (0/1)
- post_hour
- day_of_week
- caption_length
- hashtags_count

## METRICS
- reach: how many unique people a post is shown to
- follower_count
- engagement_rate: (likes + comments + shares + saves) / total impressions --> we know this bc i calc'ed it
- impressions: how many times a post comes up on a screen (not unique)
- followers_gained

## EXCLUDED SPECIFICATIONS
- post_datetime: too much info, hard to watch trend because we aren't tracking one account at a time, you can't replicate the date, waiting months to post < posting now
- post_date: you can't replicate the date, waiting months to post < posting now
- performance_bucket_list: too vague, engagement_rate is a better performance indicator

## EXCLUDED METRICS:
Likes, comments, shares, saves do not provide value alone.  These metrics are combined in the engagement_rate.

==============================================
# PART TWO: coming soon

from src.utils.file_storage import save_json_data
from src.utils.helper_functions import get_value


def extract_data_from_hashtag_api(api_responses):
    # Extract the necessary data from the API responses
    api_data = api_responses
    return api_data

def extract_data_from_keyword_api(api_responses):
    # Extract the necessary data from the API responses
    api_data = api_responses
    return api_data


def parse_tiktok_api_by_hashtag(api_responses):
    # Parse the TikTok API responses and extract necessary information
    video_data = {}
    author_data = {}
    api_data_list = extract_data_from_hashtag_api(api_responses)

    video_data_list = []
    author_data_list = []

    for api_data in api_data_list:
        all_video_data = get_value(api_data, 'itemList')

        for video in all_video_data:
            # Extract the necessary information from the video data
            video_id = get_value(video, 'id')
            author_username = get_value(video, 'author', 'uniqueId')
            video_url = 'https://www.tiktok.com/@' + author_username + '/video/' + video_id
            video_caption = get_value(video, 'desc')

            # author info
            follower_count = get_value(video, 'authorStats', 'followerCount')
            following_count = get_value(video, 'authorStats', 'followingCount')
            like_count = get_value(video, 'authorStats', 'heartCount')

            video_data_list.append({
                "video_url": video_url,
                "video_caption": video_caption,
                "author_username": author_username
            })

            author_data_list.append({
                "username": author_username,
                "follower_count": follower_count,
                "following_count": following_count,
                "like_count": like_count
            })

    # Add the extracted data to the dictionary
    video_data["video_data"] = video_data_list
    author_data["author_data"] = author_data_list

    return video_data, author_data

def parse_tiktok_api_by_keyword(api_responses):
    # Parse the TikTok API responses and extract necessary information
    video_data = {}
    author_data = {}
    api_data_list = extract_data_from_keyword_api(api_responses)

    video_data_list = []
    author_data_list = []

    for api_data in api_data_list:
        all_video_data = get_value(api_data, 'data')
        for video_item in all_video_data:
            if get_value(video_item, 'item') is not None:
                video = get_value(video_item, 'item')
                # Extract the necessary information from the video data
                video_id = get_value(video, 'id')
                author_username = get_value(video, 'author', 'uniqueId')
                video_url = 'https://www.tiktok.com/@' + author_username + '/video/' + video_id
                video_caption = get_value(video, 'desc')

                # author info
                follower_count = get_value(video, 'authorStats', 'followerCount')
                following_count = get_value(video, 'authorStats', 'followingCount')
                like_count = get_value(video, 'authorStats', 'heartCount')


                video_data_list.append({
                    "video_url": video_url,
                    "video_caption": video_caption,
                    "author_username": author_username
                })

                author_data_list.append({
                    "username": author_username,
                    "follower_count": follower_count,
                    "following_count": following_count,
                    "like_count": like_count
                })

    # Add the extracted data to the dictionary
    video_data["video_data"] = video_data_list
    author_data["author_data"] = author_data_list

    return video_data, author_data
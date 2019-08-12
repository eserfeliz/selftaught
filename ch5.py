def list_of_musicians():
    return ['Radiohead', 'Sheer Mag', 'Big Thief', 'Tame Impala']


def list_of_places_i_have_visited():
    return [(64.80805, 23.77716), (10.641818, -61.198148), (43.5890, 79.6441)]


def personal_attributes():
    return {"height": "5'9", "favorite_color": "green", "favorite_author": "Chuck Palahniuk"}


def query_attributes():
    response = input('Which characteristic about the author would you like to know more about: height, favorite color '
                     'or favorite author? ')
    response = response.lower()
    if 'height' in response:
        return query_attributes()['height']
    elif 'color' in response:
        return query_attributes()['favorite_color']
    elif 'author' in response:
        return personal_attributes()['favorite_author']
    else:
        return "I have no knowledge of {}.".format(response)


def musicians_to_favorite_songs():
    musicians_to_songs = dict()
    for artist in list_of_musicians():
        musicians_to_songs.update({artist: ''})
        if artist == 'Radiohead':
            musicians_to_songs['Radiohead'] = ['All I Need', 'Just', 'Paranoid Android']
        elif artist == 'Sheer Mag':
            musicians_to_songs['Sheer Mag'] = ['Just Can\'t Get Enough', 'Fan the Flames']
        elif artist == 'Big Thief':
            musicians_to_songs['Big Thief'] = ['Shark Smile', 'Mary']
        elif artist == 'Tame Impala':
            musicians_to_songs['Tame Impala'] = ['The Less I Know The Better', 'Let It Happen']
        else:
            pass
    return musicians_to_songs


print(musicians_to_favorite_songs())

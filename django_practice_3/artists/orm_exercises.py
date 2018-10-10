from artists.models import Artist, Song


def task_1_artist_exists():
    """Should return True if there's any artist called Eric Clapton, or False otherwise"""
    return Artist.objects.filter(artistic_name='Eric Clapton').exists()


def task_2_first_song_ordered():
    """Should return the first Song ordered by title"""
    return Song.objects.all().order_by('title').first()


def task_3_last_artist_ordered():
    """Should return the last Artist ordered by artistic_name"""
    return Artist.objects.all().order_by('artistic_name').last()


def task_4_artist_songs_contains():
    """Should return all songs from artist whose artistic names contains the letter X"""
    return Song.objects.filter(artist__artistic_name__icontains='X')


def task_5_songs_exclude():
    """Should return all songs excluding the ones that contains the word 'Castle' in its title"""
    return Song.objects.exclude(title__icontains='Castle')


def task_6_artist_name_starts_with():
    """Should return the amount of artists whose artistic name starts with the pattern 'Ji'"""
    return Artist.objects.filter(artistic_name__startswith='Ji').count()


def task_7_get_or_create_artist():
    """
        Should check if Artist 'Eric Clapton' exists in the DB and create it if
        it doesn't. Return True if you had to create, or False otherwise.
    """
    artist, created = Artist.objects.get_or_create(artistic_name='Eric Clapton', defaults={'popularity': 0})
    return created

def task_8_artist_songs_reverse_relationship():
    """Should return all songs from artist Stevie Wonders using reverse relationships"""
    artist = Artist.objects.get(artistic_name='Stevie Wonders')
    return artist.song_set.all()


def task_9_update_song_artist():
    """Should create a new Artist and assign it as the owner of the song called Superstition"""
    artist = Artist.objects.create(artistic_name='Fake Stevie Wonder', popularity=0)
    song = Song.objects.get(title='Superstition')
    song.artist = artist
    song.save()

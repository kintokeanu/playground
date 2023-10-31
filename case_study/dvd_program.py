#!/usr/bin/env python3

def calculate_total_cost(new_videos, old_videos):
    """
    Calculate the total cost for video rentals.

    Args:
    - new_videos (int): Number of new videos.
    - old_videos (int): Number of old videos.

    Returns:
    - float: Total cost of video rentals.

    Examples:
    >>> calculate_total_cost(2, 3)
    12
    """
    new_video_cost = 3 * new_videos
    old_video_cost = 2 * old_videos

    total_cost = new_video_cost + old_video_cost
    return total_cost

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Input values from user
    new_videos = int(input("Enter the number of new videos rented: "))
    old_videos = int(input("Enter the number of old videos rented: "))

    # Calculate total cost
    total_cost = calculate_total_cost(new_videos, old_videos)

    # Display the total cost
    print(f"The total cost of the videos is: ${total_cost:.2f}")

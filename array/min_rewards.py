# For a given array represents the line in which students are sitting
# we re also given reward points
# you are teacher and you want to reward the students
# o(n^2) time | O(n) space
# visit back later

arr = [8, 4, 2, 1, 3, 6, 7, 9, 5]
reward_points = 25


def min_rewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)


def min_reward_minmax_approach(scores):
    """O(N) | O(N)
    """
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i - 1] < scores[i]:
            rewards[i] = rewards[i - 1] + 1

    for i in range(len(scores) - 2, -1, -1):
        if scores[i + 1] < scores[i]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)


if __name__ == "__main__":
    print(f"************************* {min_reward_minmax_approach(arr)}")
    print(f"************************* {min_rewards(arr)}")

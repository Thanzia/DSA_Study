#divide players into teams of equal skill

'''You are given a positive integer array skill of even length n where skill[i]
denotes the skill of the ith player.Divide the players into n / 2 teams of
size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of
the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if
there is no way to divide the players into teams such that the total
skill of each team is equal.'''

#brute force t.c: O(n!)

from itertools import permutations

def divide_players_brute_force(skill):
    n = len(skill)
    total_sum = sum(skill)
    
    # If total sum can't be evenly divided into teams with equal skills
    if total_sum % (n // 2) != 0:
        return -1

    target_team_sum = total_sum // (n // 2)

    # Check all permutations of players to form pairs
    for perm in permutations(skill):
        chemistry = 0
        valid = True
        
        for i in range(0, n, 2):
            team_sum = perm[i] + perm[i + 1]
            if team_sum != target_team_sum:
                valid = False
                break
            chemistry += perm[i] * perm[i + 1]
        
        if valid:
            return chemistry
    
    return -1

# Example Usage:
skill = [3, 2, 5, 1, 3, 4]
print(divide_players_brute_force(skill))  # Output: 22

#optimal soln t.c:O(nlogn) s.c: O(1)

def divide_players_optimal(skill):
    skill.sort()  # Sort the array to make pairing easier
    n = len(skill)
    total_chemistry = 0
    team_skill = skill[0] + skill[-1]
    # This will be the sum for every valid team

    # Use two pointers to form teams
    left = 0
    right = n - 1
    
    while left < right:
        current_team_skill = skill[left] + skill[right]
        
        # Check if the current pair forms a valid team
        if current_team_skill != team_skill:
            return -1  # Return -1 if any team doesn't meet the target skill sum
        
        # Add the chemistry (product of skills) for this pair
        total_chemistry += skill[left] * skill[right]
        
        # Move the pointers inward
        left += 1
        right -= 1
    
    return total_chemistry


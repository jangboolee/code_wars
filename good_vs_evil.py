def good_vs_evil(good, evil):
    
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]
    
    good_sum = sum(g_worth * int(g_num) for g_worth, g_num in zip(good_worth, good.split()))
    evil_sum = sum(e_worth * int(e_num) for e_worth, e_num in zip(evil_worth, evil.split()))
    
    if good_sum > evil_sum:
        return "Battle Result: Good triumphs over Evil"
    elif good_sum < evil_sum:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
 

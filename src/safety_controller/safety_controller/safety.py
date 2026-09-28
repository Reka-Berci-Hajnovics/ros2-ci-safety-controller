def limit_velocity(requested_velocity, obstacle_distance):
    if obstacle_distance < 0.5:
        return 0.0

    if obstacle_distance < 1.0:
        return requested_velocity * 0.5

    return requested_velocity

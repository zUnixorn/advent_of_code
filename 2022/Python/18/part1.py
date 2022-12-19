def solution(voxels):
    neighbour_offsets = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]

    voxels = set(voxels)

    sides = 0

    for voxel in voxels:
        for neighbour_offset in neighbour_offsets:
            if tuple(map(sum, zip(voxel, neighbour_offset))) not in voxels:
                sides += 1

    return sides
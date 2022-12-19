def solution(voxels):
    neighbour_offsets = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]

    max_voxel = tuple((max(voxels, key=lambda v: v[i])[i] + 1 for i in range(3)))
    min_voxel = tuple((min(voxels, key=lambda v: v[i])[i] - 1 for i in range(3)))

    outer_space = set()
    last = set([max_voxel])

    # essentially the same algorythm, I already came up with here: https://github.com/IIRRS/z_playground/blob/optimized/src/main.rs
    # basically just do a flood fill
    while True:
        new = set()

        for voxel in last:
            for neighbour_offset in neighbour_offsets:
                neighbour_voxel = tuple(map(sum, zip(voxel, neighbour_offset)))

                if not all((min_voxel[i] <= neighbour_voxel[i] <= max_voxel[i] for i in range(3))) or neighbour_voxel in voxels:
                    continue

                new.add(neighbour_voxel)

        last = new.difference(outer_space)

        if len(last) == 0:
            break

        outer_space.update(last)

    sides = 0
    for voxel in voxels:
        for neighbour_offset in neighbour_offsets:
            neighbour_voxel = tuple(map(sum, zip(voxel, neighbour_offset)))
            if neighbour_voxel not in voxels and neighbour_voxel in outer_space:
                sides += 1

    return sides
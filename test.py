inputs = "cbbbcacc"

def answer():
    a = []
    if inputs:
        # a.append()
        count = 0
        for i in range(1, len(inputs)):
            if inputs[i - 1] != inputs[i]:
                # a.append((inputs[i], inputs.))

    # a = [(c, 1)]
    return a










# sample = [1, 3, 3, 2]

# def distinct(sample):
#     m = list()
#     for i in sample:
#         if i not in m:
#             m.append(i)
#     # m = [sample[0]]
#     # for i in range(1, len(sample)):
#     #     if sample[i] not in m:
#     #         m.append(sample[i])

#     return m

# print(distinct(sample))

# sample = [1, 2, 2, 3, 3, 3, 2 , 1, 3]

# def dedupe(sample):
#     m = []
#     if sample:
#         m.append(sample[0])
#         for i in range(1, len(sample)):
#             if sample[i - 1] != sample[i]:
#                 m.append(sample[i])

#     return m

# print(dedupe(sample))
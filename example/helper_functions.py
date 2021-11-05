def extract_cluster_frames(t, dtraj):
    '''Extract frames that are within the clusters.'''
    t_clusters = []
    mapping = {}
    for x in np.unique(dtraj):
        mapping[x] = np.where(dtraj == x)[0]
    
    for x in mapping:
        t_clusters.append(t[mapping[x]])
    
    return t_clusters


def cluster_center(clustering, data_in):
    '''Find cluster centers from trajectory input data.'''
    mapping = clustering._labels.mapping
    n_clusters = len(mapping)
    
    centers = []
    for i in range(1, n_clusters):
        c_data = data_in[np.array(mapping[i])]
        m = np.mean(c_data, axis=0)
        centers.append(m)
        
    return centers


def closest_to_center(center, data_in):
    '''Return index of input traj that is closest to cluster center.'''
    c_dist_in = np.array([np.linalg.norm(x - center) for x in data_in])
    return np.argmin(c_dist_in)
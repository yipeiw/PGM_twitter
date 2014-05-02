function Y=load_label(filepath, node_map)
data=csvread(filepath);
nInstances=size(data, 1);
nNodes = size(node_map);

Y=zeros(nInstances, nNodes);
for i=1:nInstances
    [r,c,v] = find(data(i, :));
    for j=1:length(v)
        idx = node_map.get(v(j));
        Y(i, idx) = 1;
    end
end

Y = int32(Y+1);
end

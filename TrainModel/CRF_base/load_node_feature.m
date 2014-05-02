function [Xnode, nodeMap] = load_node_feature(filelist, nInstances, nNodes, nFeatures, node_map)
Xnode = zeros(nInstances, nFeatures, nNodes);

list=load_files(filelist);
for n=1:length(list)
    [pathstr,name,ext] = fileparts(list{n});
    node_idx = node_map.get(str2num(name));
    Xnode(:, :, node_idx) = csvread(list{n});
end

nodeMap = zeros(nNodes, 2, nFeatures, 'int32');
for f=1:nFeatures
    nodeMap(:,1,f) = f;
end

end

function names=load_files(filelist)
fid = fopen(filelist);

count = 1;
while 1
    tline = fgetl(fid);
    if ~ischar(tline)
        break
    end
    names{count} = tline;
    count  = count + 1;
end

fclose(fid);
end

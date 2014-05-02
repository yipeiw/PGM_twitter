function [Xedge, edgeMap]=load_edge_feature(staticfile, dfile, nInstances, nFeatures, startIdx, edgeStruct, node_map, edge_map)
nEdges = edgeStruct.nEdges;

%push into static feature
static_feat=csvread(staticfile);  s_num = size(static_feat, 1)
Xedge=zeros(nInstances, nFeatures, nEdges);
for i=1:s_num
    n1=node_map.get(static_feat(i, 1)); n2 = node_map.get(static_feat(i, 2));
    feat=static_feat(i, 3:end);
    edgeIdx = edge_map.get(num2str([n1, n2]));
    Xedge(:, :, edgeIdx) = repmat(feat, nInstances, 1);
end
%push into other feature, not use it now
%feat = csvread(dfile);

edgeMap = zeros(2, 2, nEdges, nFeatures, 'int32');
f=startIdx;
for edgeFeat=1:nFeatures
    edgeMap(1,1,:,edgeFeat) = f;
    edgeMap(1,2,:,edgeFeat) = f+1;
    edgeMap(2,1,:,edgeFeat) = f+2;
    edgeMap(2,2,:,edgeFeat) = f+3;
    f=f+4;
end

end


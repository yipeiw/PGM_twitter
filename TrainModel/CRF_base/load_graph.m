function [edgeStruct, node_map, edge_map]=load_graph(relationfile)
R = csvread(relationfile); num = size(R, 1);
nodes = unique(R(:)); nNodes = length(nodes)

node_map = java.util.Hashtable;
for i=1:nNodes
    node_map.put(nodes(i), i);
end

adj = zeros(nNodes);
for i=1:num
    idx1 = node_map.get(R(i, 1));
    idx2 = node_map.get(R(i, 2));
    adj(idx1, idx2) = 1; adj(idx2, idx1) = 1;
end

nStates=2;
edgeStruct = UGM_makeEdgeStruct(adj, nStates);
edge_map = getmap(edgeStruct);

end

function edge_map=getmap(edgeStruct)
nEdges=edgeStruct.nEdges;
edge_map = java.util.Hashtable;

for i=1:nEdges
    nodes=edgeStruct.edgeEnds(i, :);
    edge_map.put(num2str([nodes(1), nodes(2)]), i);
    edge_map.put(num2str([nodes(2), nodes(1)]), i);
end

end

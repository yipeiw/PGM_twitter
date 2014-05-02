%construct graph structure (follower relation)
relationfile = '/home/yipei/Twitter/ExtractGraph/graphs/29087161_s2.csv';
[edgeStruct, node_map, edge_map] = load_graph(relationfile);

edgeStruct.nEdges
length(edge_map.values())

%load data
labelfile='/home/yipei/Twitter/FeatureExtraction/data/label/29087161_s2.csv';
Y = load_label(labelfile, node_map);
[nInstances, nNodes] = size(Y)

%representing feature
nFeatures=12;
feat_path='/home/yipei/Twitter/FeatureExtraction/data/trainfile/CRFbase/29087161_s2';
node_file_list = strcat(feat_path, '/node.list');
[Xnode, nodeMap] = load_node_feature(node_file_list, nInstances, nNodes, nFeatures, node_map);
lastFeatIdx = max(nodeMap(:));

nEdgeFeature=3; %3 bias, 1 (can ignore currently)
edgefile_static=strcat(feat_path, '/edge_static.csv');
edgefile=strcat(feat_path, '/edge_coretweet.csv');
[Xedge, edgeMap] = load_edge_feature(edgefile_static, edgefile, nInstances, nEdgeFeature, lastFeatIdx, edgeStruct, node_map, edge_map);

%objective function
nParams = max([nodeMap(:); edgeMap(:)]);
w = zeros(nParams,1);

%lambda=10*ones(size(w));
%lambda(lastFeatIdx+1:lastFeatIdx+3)=0;
lambda=zeros(size(w));

%there are some user features in the node feature that should not be penalized
runFunObj = @(w)penalizedL2(w,@UGM_CRF_NLL,lambda,Xnode,Xedge,Y,nodeMap,edgeMap,edgeStruct,@UGM_Infer_LBP);

%optimize
w=minFunc(runFunObj, w);

%test performance
%[nodePot, edgePot] = UGM_CRF_makePotentials(w, Xnode, Xedge, nodeMap, edgeMap, edgeStruct, i);
%optimal = UGM_Decode_Exact(nodePot, edgePot, edgeStruct);

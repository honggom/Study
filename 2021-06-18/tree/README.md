## 1. 트리 구조
- Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
- 실제로 어디에 많이 사용되나 :<br>
    - 트리 중 이진 트리 (Binary Tree) 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용됨

## 2. 트리의 용어
- Node : 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 Node에 대한 Branch 정보 포함)
- Root Node : 트리 맨 위에 있는 노드
- Level : root node를 level 0으로 하였을 때, 하위 branch로 연결되 노드의 깊이를 나타냄
- Parent Node : 어떤 node의 이전 레벨에 연결된 node
- Child Node : 어떤 node의 다음 레벨에 연결된 node
- Leaf Node : child node가 하나도 없는 node
- Sibling : 동일한 Parent Node를 가진 node
- Depth : 트리에서 node가 가질 수 있는 최대 level
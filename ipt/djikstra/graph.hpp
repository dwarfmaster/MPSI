
#ifndef DEF_GRAPH
#define DEF_GRAPH

#include <vector>

struct Node;
struct Link
{
    Node* node;
    unsigned int length;
};
struct Node
{
    std::vector<Link> links;
    unsigned int sum;
    std::vector<unsigned int> path;
};

class Graph
{
    public:
        Graph();
        ~Graph();

        Node* root();
        Node* create_children(Node* parent, unsigned int length);
        void link(Node* n1, Node* n2, unsigned int length);

    private:
        Node m_root;
};

#endif


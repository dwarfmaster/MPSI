#include "graph.hpp"
#define NULL 0

Graph::Graph()
{
    m_root.links.clear();
    m_root.sum = 0;
    m_root.path.clear();
}

static void free_node(Node** n)
{
    for(unsigned int i = 0; i <= (*n)->links.size(); ++i) {
        Node** temp = &(*n)->links[i].node;
        if(*temp != NULL)
            free_node(temp);
    }
    delete *n;
    *n = NULL;
}

Graph::~Graph()
{
    Node* p = &m_root;
    free_node(&p);
}

Node* Graph::root()
{
    return &m_root;
}

Node* Graph::create_children(Node* parent, unsigned int length)
{
    Node* child = new Node;
    child->links.clear();
    child->sum = 0;
    child->path.clear();
    
    Link lnk;
    lnk.node = child;
    lnk.length = length;
    parent->links.push_back(lnk);

    return child;
}

void Graph::link(Node* n1, Node* n2, unsigned int length)
{
    Link lnk;
    lnk.node = n2;
    lnk.length = length;
    n1->links.push_back(lnk);
}


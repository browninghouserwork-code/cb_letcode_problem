

const tree1 = {
    val: 1,
    left: {
        val: 2,
        left: null,
        right: null
    },
    right: {
        val: 3,
        left: null,
        right: null
    }
};

const tree2 = {
    val: 1,
    left: {
        val: 2,
        left: null,
        right: null
    },
    right: {
        val: 3,
        left: null,
        right: null
    }
};
const tree3 = {
    val: 1,
    left: {
        val: 2,
        left: null,
        right: null
    },
    right: null
};


var isSameTree = function(p, q) {
    
    if( p === null && q === null ) 
         return true;
    if( p == null || q == null || p.val !== q.val ) 
        return false;

    return isSameTree(p.left,q.left) && isSameTree(p.right, q.right);
};

console.log(isSameTree(tree1, tree3));  // Output: false

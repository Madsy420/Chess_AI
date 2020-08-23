#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Remember, this project is not a full chess game simulator, but can deifinietly be done, with another driver function.
"""
import copy
from multiprocessing.pool import ThreadPool


# In[2]:


"""This class makes an instance of a chess board and has the necessary 
functions to store the states of the board and process it."""

class chess:
    
    """This function has the following function: it converts the chess board positions to coordinates, 
    eg: b4 -> (4,2)"""
    def pos_to_coord(self,a):
        c = a[0]
        row = int(a[1])
        k = enumerate(['a','b','c','d','e','f','g','h'],1)
        for i,j in k:
            if j == c:
                col = i
                break
                
        return [row,col]
    
    
    """This function has the opposite function of the pos_to_coord function i.e.
    eg: (4,2) -> b4"""
    def coord_to_pos(self,a):

        k = enumerate(['a','b','c','d','e','f','g','h'],1)
        #print(a)
        for i,j in k:
            if i == a[1]:
                col = j
                break
        
        return col + str(a[0])
    
    
    """A function to initalise a board with proper start game states"""
    def init_board(self):
        
        """
        record:
        "board": Stores the board states(given below as self.board).
        "side" : Which side is to play next.
        "check": Whether the king is under check. 
        """
        self.record = {
            "board":None,
            "side" :None,
            "check":None
        }
        
        """
        board:
        "w"  : shows info about all the white pieces.
        "b"  : shows info about all the black pieces.
        "is_occupied": has info about which squares on the board are occupied.
        """
        
        self.board = {
            "w" :None,
            "b" :None,
            "is_occupied" : None
        }
        
        """
        notation is as follows: 
        p1,p2.......p8 -> pawn 1, pawn 2......pawn 8 (p -> pawn)
        r1,r2 -> rook 1, rook 2 (r -> rook)
        k1,k2 -> knight 1, knight 2 (k -> knight)
        b1,b2 -> bishop 1, bishop 2 (b -> bishop)
        q -> queen
        king....yeah, just that
        "is occupied": has all the square names.
        "typ": type of piece.
        "st_pos": starting position of the piece.
        "cr_pos": current position.
        "score" : number of points the piece is worth.
        "on_brd": tells if the piece is still on board.
        "has_mvd": This is only available for king and rook pieces, used to check possibiliteis of castling.
        """
        self.board["w"] = {
            "p1" :None,
            "p2" :None,
            "p3" :None,
            "p4" :None,
            "p5" :None,
            "p6" :None,
            "p7" :None,
            "p8" :None,
            "r1" :None,
            "r2" :None,
            "k1" :None,
            "k2" :None,
            "b1" :None,
            "b2" :None,
            "q"  :None,
            "king"  :None
        }
        self.board["b"] = {
            "p1" :None,
            "p2" :None,
            "p3" :None,
            "p4" :None,
            "p5" :None,
            "p6" :None,
            "p7" :None,
            "p8" :None,
            "r1" :None,
            "r2" :None,
            "k1" :None,
            "k2" :None,
            "b1" :None,
            "b2" :None,
            "q"  :None,
            "king"  :None
        }
        self.board["is_occupied"] = {
            "a1" : True,
            "b1" : True,
            "c1" : True,
            "d1" : True,
            "e1" : True,
            "f1" : True,
            "g1" : True,
            "h1" : True,
            "a2" : True,
            "b2" : True,
            "c2" : True,
            "d2" : True,
            "e2" : True,
            "f2" : True,
            "g2" : True,
            "h2" : True,
            "a3" : False,
            "b3" : False,
            "c3" : False,
            "d3" : False,
            "e3" : False,
            "f3" : False,
            "g3" : False,
            "h3" : False,
            "a4" : False,
            "b4" : False,
            "c4" : False,
            "d4" : False,
            "e4" : False,
            "f4" : False,
            "g4" : False,
            "h4" : False,
            "a5" : False,
            "b5" : False,
            "c5" : False,
            "d5" : False,
            "e5" : False,
            "f5" : False,
            "g5" : False,
            "h5" : False,
            "a6" : False,
            "b6" : False,
            "c6" : False,
            "d6" : False,
            "e6" : False,
            "f6" : False,
            "g6" : False,
            "h6" : False,
            "a7" : True,
            "b7" : True,
            "c7" : True,
            "d7" : True,
            "e7" : True,
            "f7" : True,
            "g7" : True,
            "h7" : True,
            "a8" : True,
            "b8" : True,
            "c8" : True,
            "d8" : True,
            "e8" : True,
            "f8" : True,
            "g8" : True,
            "h8" : True
            
        }

        self.board["w"]["p1"] = {
            "typ"    : 'p',
            "st_pos" : 'a2',
            "cr_pos" : 'a2',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["w"]["p2"] = {
            "typ"    : 'p',
            "st_pos" : 'b2',
            "cr_pos" : 'b2',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["w"]["p3"] = {
            "typ"    : 'p',
            "st_pos" : 'c2',
            "cr_pos" : 'c2',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["w"]["p4"] = {
            "typ"    : 'p',
            "st_pos" : 'd2',
            "cr_pos" : 'd2',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["w"]["p5"] = {
            "typ"    : 'p',
            "st_pos" : 'e2',
            "cr_pos" : 'e2',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["w"]["p6"] = {
            "typ"    : 'p',
            "st_pos" : 'f2',
            "cr_pos" : 'f2',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["w"]["p7"] = {
            "typ"    : 'p',
            "st_pos" : 'g2',
            "cr_pos" : 'g2',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["w"]["p8"] = {
            "typ"    : 'p',
            "st_pos" : 'h2',
            "cr_pos" : 'h2',
            "score"  : 3,
            "on_brd" : True
        }
        
        ######################################
        
        self.board["w"]["r1"] = {
            "typ"    : 'r',
            "st_pos" : 'a1',
            "cr_pos" : 'a1',
            "score"  : 20,
            "on_brd" : True,
            "has_mvd": False
        }
        self.board["w"]["k1"] = {
            "typ"    : 'k',
            "st_pos" : 'b1',
            "cr_pos" : 'b1',
            "score"  : 12,
            "on_brd" : True
        }
        self.board["w"]["b1"] = {
            "typ"    : 'b',
            "st_pos" : 'c1',
            "cr_pos" : 'c1',
            "score"  : 12,
            "on_brd" : True
        }
        self.board["w"]["q"] = {
            "typ"    : 'q',
            "st_pos" : 'd1',
            "cr_pos" : 'd1',
            "score"  : 40,
            "on_brd" : True
        }
        self.board["w"]["king"] = {
            "typ"    : 'king',
            "st_pos" : 'e1',
            "cr_pos" : 'e1',
            "score"  : 500,
            "on_brd" : True,
            "has_mvd": False,
            "castle" : False
        }
        self.board["w"]["b2"] = {
            "typ"    : 'b',
            "st_pos" : 'f1',
            "cr_pos" : 'f1',
            "score"  : 12,
            "on_brd" : True
        }
        self.board["w"]["k2"] = {
            "typ"    : 'k',
            "st_pos" : 'g1',
            "cr_pos" : 'g1',
            "score"  : 12,
            "on_brd" : True
        }
        self.board["w"]["r2"] = {
            "typ"    : 'r',
            "st_pos" : 'h1',
            "cr_pos" : 'h1',
            "score"  : 20,
            "on_brd" : True,
            "has_mvd": False
        }
        
        ######################################
        ######################################
        
        self.board["b"]["p1"] = {
            "typ"    : 'p',
            "st_pos" : 'a7',
            "cr_pos" : 'a7',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["b"]["p2"] = {
            "typ"    : 'p',
            "st_pos" : 'b7',
            "cr_pos" : 'b7',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["b"]["p3"] = {
            "typ"    : 'p',
            "st_pos" : 'c7',
            "cr_pos" : 'c7',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["b"]["p4"] = {
            "typ"    : 'p',
            "st_pos" : 'd7',
            "cr_pos" : 'd7',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["b"]["p5"] = {
            "typ"    : 'p',
            "st_pos" : 'e7',
            "cr_pos" : 'e7',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["b"]["p6"] = {
            "typ"    : 'p',
            "st_pos" : 'f7',
            "cr_pos" : 'f7',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["b"]["p7"] = {
            "typ"    : 'p',
            "st_pos" : 'g7',
            "cr_pos" : 'g7',
            "score"  : 3,
            "on_brd" : True
        }
        self.board["b"]["p8"] = {
            "typ"    : 'p',
            "st_pos" : 'h7',
            "cr_pos" : 'h7',
            "score"  : 3,
            "on_brd" : True
        }
        
        ######################################
        
        self.board["b"]["r1"] = {
            "typ"    : 'r',
            "st_pos" : 'a8',
            "cr_pos" : 'a8',
            "score"  : 20,
            "on_brd" : True,
            "has_mvd": False
        }
        self.board["b"]["k1"] = {
            "typ"    : 'k',
            "st_pos" : 'b8',
            "cr_pos" : 'b8',
            "score"  : 12,
            "on_brd" : True
        }
        self.board["b"]["b1"] = {
            "typ"    : 'b',
            "st_pos" : 'c8',
            "cr_pos" : 'c8',
            "score"  : 12,
            "on_brd" : True
        }
        self.board["b"]["q"] = {
            "typ"    : 'q',
            "st_pos" : 'd8',
            "cr_pos" : 'd8',
            "score"  : 40,
            "on_brd" : True
        }
        self.board["b"]["king"] = {
            "typ"    : 'king',
            "st_pos" : 'e8',
            "cr_pos" : 'e8',
            "score"  : 500,
            "on_brd" : True,
            "has_mvd": False,
            "castle" : False
        }
        self.board["b"]["b2"] = {
            "typ"    : 'b',
            "st_pos" : 'f8',
            "cr_pos" : 'f8',
            "score"  : 12,
            "on_brd" : True
        }
        self.board["b"]["k2"] = {
            "typ"    : 'k',
            "st_pos" : 'g8',
            "cr_pos" : 'g8',
            "score"  : 12,
            "on_brd" : True
        }
        self.board["b"]["r2"] = {
            "typ"    : 'r',
            "st_pos" : 'h8',
            "cr_pos" : 'h8',
            "score"  : 20,
            "on_brd" : True,
            "has_mvd": False
        }
        ##################################
    
    """
    piece_pos: returns the positon of all the pieces on the board
    returns a dictionary:
    pos["w"] -> white piece positions
    pos["b"] -> black piece positions
    """
    
    def piece_pos(self):
        pieces = enumerate(["p1","p2","p3","p4","p5","p6","p7","p8","r1","k1","b1","q","king","b2","k2","r2"])
        w_pos = set()
        b_pos = set()
        for i in range(16):
            for num,piece in pieces:
                if num == i:
                    ch = piece
                    break
            if self.board["w"][ch]["on_brd"]:
                w_pos.add(self.board["w"][ch]["cr_pos"])
                
            if self.board["b"][ch]["on_brd"]:
                b_pos.add(self.board["b"][ch]["cr_pos"])
        pos = {
            "w" : w_pos,
            "b" : b_pos
        }
        
        return pos
    
    """
    piece_at_pos:
    gives the piece at a postion. returns a dictionary:
    result["side"]: side of the piece on the square.
    result["piece"]: type of piece on that square.
    result["name"]: name of the piece w.r.t to the dictionary(notations given before)
    """
    def piece_at_pos(self,pos):
        pieces =["p1","p2","p3","p4","p5","p6","p7","p8","r1","k1","b1","q","king","b2","k2","r2"]

        for pc in pieces:
            if self.board["w"][pc]["cr_pos"] == pos:
                side = "w"
                piece = self.board["w"][pc]
                #print(pc)
                break
            elif self.board["b"][pc]["cr_pos"] == pos:
                side = "b"
                piece = self.board["b"][pc]
                break
        result = {
            "side" : side,
            "piece": piece,
            "name" : pc
        } 
        return result
    
    """
    gives the piece and the side it belongs to, It will use this to return all possible moves for that piece.
    returns a dictionary:
    result["pos_pos"]: possible poisitons
    result["protects"]: pieces it protects(i.e. pieces from the same side that it can reach if taken.)
    """
    def pos_moves(self,piece,side):
        
        states = []
        pos_pos = []
        protects = []
        brd = self.board
        cr_pos = piece["cr_pos"]
        
        typ = piece["typ"]
        cur_coord = self.pos_to_coord(cr_pos)
        
        #possible moves if the piece is a pawn
        if typ == 'p':
            #possible moves if the pawn is white
            if side == 'w':
                if cur_coord[0] == 2:
                    temp_pos = self.coord_to_pos([cur_coord[0]+1,cur_coord[1]])
                    if not(self.board["is_occupied"][temp_pos]):
                        pos_pos.append(temp_pos)
                    temp_pos = self.coord_to_pos([cur_coord[0]+2,cur_coord[1]])
                    if not(self.board["is_occupied"]):
                        pos_pos.append(temp_pos)
                    
                elif 2 < cur_coord[0] <= 7:                   
                    temp_pos = self.coord_to_pos([cur_coord[0]+1,cur_coord[1]])
                    if not(self.board["is_occupied"][temp_pos]):
                        pos_pos.append(temp_pos)
                        
                if cur_coord[1] == 1:
                    temp_pos = self.coord_to_pos([cur_coord[0]+1,cur_coord[1]+1])
                    if self.board["is_occupied"][temp_pos]:
                        if self.piece_at_pos(temp_pos)["side"] != side:
                            pos_pos.append(temp_pos)
                        else:
                            protects.append(temp_pos)
                elif cur_coord[1] == 8:
                    temp_pos = self.coord_to_pos([cur_coord[0]+1,cur_coord[1]-1])
                    if self.board["is_occupied"][temp_pos]:
                        if self.piece_at_pos(temp_pos)["side"] != side:
                            pos_pos.append(temp_pos)
                        else:
                            protects.append(temp_pos)
                elif 2 < cur_coord[1] <= 7:
                    temp_pos = self.coord_to_pos([cur_coord[0]+1,cur_coord[1]+1])
                    if self.board["is_occupied"][temp_pos]:
                        if self.piece_at_pos(temp_pos)["side"] != side:
                            pos_pos.append(temp_pos)
                        else:
                            protects.append(temp_pos)
                    temp_pos = self.coord_to_pos([cur_coord[0]+1,cur_coord[1]-1])
                    if self.board["is_occupied"][temp_pos]:
                        if self.piece_at_pos(temp_pos)["side"] != side:
                            pos_pos.append(temp_pos)
                        else:
                            protects.append(temp_pos)
                    
            #possible moves if the pawn is black   
            if side == 'b':
                if cur_coord[0] == 7:
                    temp_pos = self.coord_to_pos([cur_coord[0]-1,cur_coord[1]])
                    if not(self.board["is_occupied"][temp_pos]):
                        pos_pos.append(temp_pos)
                    temp_pos = self.coord_to_pos([cur_coord[0]-2,cur_coord[1]])
                    if not(self.board["is_occupied"][temp_pos]):
                        pos_pos.append(temp_pos)
                    
                elif 2 < cur_coord[0] <= 7:
                    temp_pos = self.coord_to_pos([cur_coord[0]-1,cur_coord[1]])
                    if not(self.board["is_occupied"][temp_pos]):
                        pos_pos.append(temp_pos)
                        
                if cur_coord[1] == 1:
                    temp_pos = self.coord_to_pos([cur_coord[0]-1,cur_coord[1]+1])
                    if self.board["is_occupied"][temp_pos]:
                        if self.piece_at_pos(temp_pos)["side"] != side:
                            pos_pos.append(temp_pos)
                        else:
                            protects.append(temp_pos)
                elif cur_coord[1] == 8:
                    temp_pos = self.coord_to_pos([cur_coord[0]-1,cur_coord[1]-1])
                    if self.board["is_occupied"][temp_pos]:
                        if self.piece_at_pos(temp_pos)["side"] != side:
                            pos_pos.append(temp_pos)
                        else:
                            protects.append(temp_pos)
                elif 2 < cur_coord[1] <= 7:
                    temp_pos = self.coord_to_pos([cur_coord[0]-1,cur_coord[1]+1])
                    if self.board["is_occupied"][temp_pos]:
                        if self.piece_at_pos(temp_pos)["side"] != side:
                            pos_pos.append(temp_pos)
                        else:
                            protects.append(temp_pos)
                    temp_pos = self.coord_to_pos([cur_coord[0]-1,cur_coord[1]-1])
                    if self.board["is_occupied"][temp_pos]:
                        if self.piece_at_pos(temp_pos)["side"] != side:
                            pos_pos.append(temp_pos)
                        else:
                            protects.append(temp_pos)
                    
        #gives possible moves if the piece is a knight
        if typ == "k":
            coord_pos_pos = []
            coord_pos_pos.append([cur_coord[0]+1,cur_coord[1]+2])
            coord_pos_pos.append([cur_coord[0]+1,cur_coord[1]-2])
            coord_pos_pos.append([cur_coord[0]-1,cur_coord[1]+2])
            coord_pos_pos.append([cur_coord[0]-1,cur_coord[1]-2])
            coord_pos_pos.append([cur_coord[0]+2,cur_coord[1]+1])
            coord_pos_pos.append([cur_coord[0]+2,cur_coord[1]-1])
            coord_pos_pos.append([cur_coord[0]-2,cur_coord[1]+1])
            coord_pos_pos.append([cur_coord[0]-2,cur_coord[1]-1])
            for pos in coord_pos_pos:
                if (1<=pos[0]<=8)and(1<=pos[1]<=8):
                    piece_pos = self.coord_to_pos(pos)
                    if self.board["is_occupied"][piece_pos]:
                        if side != self.piece_at_pos(piece_pos)["side"]:
                            pos_pos.append(piece_pos)
                        else:
                            protects.append(piece_pos)
                    else:
                        pos_pos.append(piece_pos)
                        
        #possible moves if the piece is a bishop 
        if typ == "b":
            diag_list_neg_neg = [[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7]]
            diag_list_pos_pos = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
            diag_list_neg_pos = [[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7]]
            diag_list_pos_neg = [[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7]]
            lis_of_lis = [diag_list_neg_neg,diag_list_pos_pos,diag_list_neg_pos,diag_list_pos_neg]
            for lis in lis_of_lis:
                for mov in lis:
                    temp_pos = [cur_coord[0]+mov[0],cur_coord[1]+mov[1]]
                    if (1<=temp_pos[0]<=8) and (1<=temp_pos[1]<=8):
                        piece_pos = self.coord_to_pos(temp_pos)
                        if self.board["is_occupied"][piece_pos]:
                            if side != self.piece_at_pos(piece_pos)["side"]:
                                pos_pos.append(piece_pos)
                            else:
                                protects.append(piece_pos)
                            break    
                        else:
                            pos_pos.append(piece_pos)
                    else:
                        break
        
        #possible moves if the piece is a rook
        if typ == "r":
            straight_list_neg_nil = [[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0]]
            straight_list_pos_nil = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]
            straight_list_nil_neg = [[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7]]
            straight_list_nil_pos = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]]
            lis_of_lis = [straight_list_neg_nil,straight_list_pos_nil,straight_list_nil_neg,straight_list_nil_pos]
            for lis in lis_of_lis:
                for mov in lis:
                    temp_pos = [cur_coord[0]+mov[0],cur_coord[1]+mov[1]]
                    
                    if (1<=temp_pos[0]<=8) and (1<=temp_pos[1]<=8):
                        piece_pos = self.coord_to_pos(temp_pos)
                        if self.board["is_occupied"][piece_pos]:
                            if side != self.piece_at_pos(piece_pos)["side"]:
                                pos_pos.append(piece_pos)
                            else:
                                protects.append(piece_pos)
                            break
                        else:
                            pos_pos.append(piece_pos)
                    else:
                        break
                        
        #possible moves if the piece is a queen
        if typ == "q":
            diag_list_neg_neg = [[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7]]
            diag_list_pos_pos = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
            diag_list_neg_pos = [[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7]]
            diag_list_pos_neg = [[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7]]
            straight_list_neg_nil = [[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0]]
            straight_list_pos_nil = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]
            straight_list_nil_neg = [[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7]]
            straight_list_nil_pos = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]]
            lis_of_lis = [diag_list_neg_neg,diag_list_pos_pos,diag_list_neg_pos,diag_list_pos_neg,straight_list_neg_nil,straight_list_pos_nil,straight_list_nil_neg,straight_list_nil_pos]
            for lis in lis_of_lis:
                for mov in lis:
                    temp_pos = [cur_coord[0]+mov[0],cur_coord[1]+mov[1]]
                    
                    if (1<=temp_pos[0]<=8) and (1<=temp_pos[1]<=8):
                        piece_pos = self.coord_to_pos(temp_pos)
                        if self.board["is_occupied"][piece_pos]:
                            if side != self.piece_at_pos(piece_pos)["side"]:
                                pos_pos.append(piece_pos)
                            else:
                                protects.append(piece_pos)
                            break
                        else:
                            pos_pos.append(piece_pos)
                    else:
                        break
                        
        #possible moves if the piece is a king
        if typ == "king":
            mov_list = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
            #pawns = ["p1","p2","p3","p4","p5","p6","p7","p8"]
            #powers = ["r1","k1","b1","q","b2","k2","r2"]
            if side == 'w':
                oppos_side = 'b'
                oppos_pos = self.piece_pos()["b"]
            else:
                oppos_side = 'w'
                oppos_pos = self.piece_pos()["w"]
            set_of_moves_dict = self.covered_squares(oppos_side)
            set_of_moves = set(set_of_moves_dict["set_of_moves"]).union(set(set_of_moves_dict["protected_squares"]))
            for mov in mov_list:
                temp_pos = [cur_coord[0]+mov[0],cur_coord[1]+mov[1]]
                
                if (1<=temp_pos[0]<=8) and (1<=temp_pos[1]<=8):
                    piece_pos = self.coord_to_pos(temp_pos)
                    if self.board["is_occupied"][piece_pos]:
                        if side != self.piece_at_pos(piece_pos)["side"]:
                            if not(piece_pos in set_of_moves):
                                pos_pos.append(piece_pos)
                        else:
                            protects.append(piece_pos)
                    else:
                        if not(piece_pos in set_of_moves):
                            pos_pos.append(piece_pos)
            
            if not(piece["has_mvd"]):
                if side == "w":
                    if not(self.board["is_occupied"]["d1"]) and not(self.board["is_occupied"]["c1"]) and not(self.board["is_occupied"]["b1"]):
                        if not(self.board["w"]["r1"]["has_mvd"]):
                            if not(("d1" in set_of_moves)or("c1" in set_of_moves)or("b1" in set_of_moves)):
                                if not(cr_pos in set_of_moves):
                                    pos_pos.append("c1")
                    if not(self.board["is_occupied"]["f1"]) and not(self.board["is_occupied"]["g1"]):
                        if not(self.board["w"]["r2"]["has_mvd"]):
                            if not(("f1" in set_of_moves)or("g1" in set_of_moves)):
                                if not(cr_pos in set_of_moves):
                                    pos_pos.append("g1")
                if side == "b":
                    if not(self.board["is_occupied"]["d8"]) and not(self.board["is_occupied"]["c8"]) and not(self.board["is_occupied"]["b8"]):
                        if not(self.board["b"]["r1"]["has_mvd"]):
                            if not(("d1" in set_of_moves)or("c8" in set_of_moves)or("b8" in set_of_moves)):
                                if not(cr_pos in set_of_moves):
                                    pos_pos.append("c8")
                    if not(self.board["is_occupied"]["f8"]) and not(self.board["is_occupied"]["g8"]):
                        if not(self.board["b"]["r2"]["has_mvd"]):
                            if not(("f8" in set_of_moves)or("g8" in set_of_moves)):
                                if not(cr_pos in set_of_moves):
                                    pos_pos.append("g8")
            
        result = {
            "pos_pos" : pos_pos,
            "protects": protects
        }                
                            
                    
                
        return result
            
    """
    This is essentially the heart of the code, it gives the possible states a board can move to, 
    if the side to move is given
    returns multiple instances of objects w.r.t to the change of possible moves that can be done.
    """
    def pos_states(self,side):
        states = []
        pieces = ["p1","p2","p3","p4","p5","p6","p7","p8","r1","k1","b1","q","king","b2","k2","r2"]
        convert = False
        if side == 'w':
            oppos_side = 'b'
        else:
            oppos_side = 'w'

        for pc in pieces:
            if self.board[side][pc]["on_brd"]:
                pos_moves_for_piece = self.pos_moves(self.board[side][pc],side)["pos_pos"]
                current_pos = self.board[side][pc]["cr_pos"]
                for mov in pos_moves_for_piece:
                    state = copy.deepcopy(self)
                    if self.board["is_occupied"][mov] == True:
                        #print(mov)
                        enemy_piece = self.piece_at_pos(mov)["name"]
                        state.board[oppos_side][enemy_piece]["on_brd"] = False
                        state.board["is_occupied"][current_pos] = False
                        #state.board["is_occupied"][mov] = True
                        state.board[side][pc]["cr_pos"] = mov
                    elif self.board["is_occupied"][mov] == "enpass":
                        if oppos_side == "w":
                            mov_coord = self.pos_to_coord(mov)
                            pawn_pos = self.coord_to_pos([mov_coord[0]+1,mov_coord[1]])
                            enemy_piece = self.piece_at_pos(pawn_pos)["name"]
                            state.board[oppos_side][enemy_piece]["on_brd"] = False
                            state.board["is_occupied"][current_pos] = False
                            state.board["is_occupied"][mov] = True
                            state.board["is_occupied"][pawn_pos] = False
                            state.board[side][pc]["cr_pos"] = mov
                        else:
                            mov_coord = self.pos_to_coord(mov)
                            pawn_pos = self.coord_to_pos([mov_coord[0]-1,mov_coord[1]])
                            enemy_piece = self.piece_at_pos(pawn_pos)["name"]
                            state.board[oppos_side][enemy_piece]["on_brd"] = False
                            state.board["is_occupied"][current_pos] = False
                            state.board["is_occupied"][mov] = True
                            state.board["is_occupied"][pawn_pos] = False
                            state.board[side][pc]["cr_pos"] = mov

                    else:
                        if self.board[side][pc]["typ"] == 'p':
                            if self.board[side][pc]["st_pos"] == current_pos:
                                if mov[1] in set([4,5]):
                                    current_coord = self.pos_to_coord(current_pos)
                                    if side == "w":
                                        enpass_pos == self.coord_to_pos([current_coord[0]+1,current_coord[1]])
                                    else:
                                        enpass_pos == self.coord_to_pos([current_coord[0]-1,current_coord[1]])
                                    state.board["is_occupied"][enpass_pos] == "enpass"
                            if side == 'w':
                                if mov[1] == '8':
                                    convert = True
                            else:
                                if mov[1] == '1':
                                    convert = True

                        if self.board[side][pc]["typ"] == "king":
                            if not(self.board[side][pc]["has_mvd"]):
                                if side == 'w':
                                    if mov == "c1":
                                        state.board["is_occupied"]["a1"] = False
                                        state.board["is_occupied"]["d1"] = True
                                        state.board["w"]["r1"]["cr_pos"] = "d1"
                                        state.board["w"]["r1"]["has_mvd"] = True
                                    if mov == "g1":
                                        state.board["is_occupied"]["h1"] = False
                                        state.board["is_occupied"]["f1"] = True
                                        state.board["w"]["r2"]["cr_pos"] = "f1"
                                        state.board["w"]["r2"]["has_mvd"] = True
                                if side == 'b':
                                    if mov == "c8":
                                        state.board["is_occupied"]["a8"] = False
                                        state.board["is_occupied"]["d8"] = True
                                        state.board["b"]["r1"]["cr_pos"] = "d8"
                                        state.board["b"]["r1"]["has_mvd"] = True
                                    if mov == "g8":
                                        state.board["is_occupied"]["h8"] = False
                                        state.board["is_occupied"]["f8"] = True
                                        state.board["b"]["r2"]["cr_pos"] = "f8"
                                        state.board["b"]["r2"]["has_mvd"] = True
                                state.board[side]["king"]["has_mvd"] = True
                                state.board[side]["king"]["castle"] = True

                        state.board["is_occupied"][current_pos] = False
                        state.board["is_occupied"][mov] = True
                        state.board[side][pc]["cr_pos"] = mov
                    if not(convert or state.check_check(side)):
                        states.append(state)
                    elif not(state.check_check(side)):
                        types = [['k',12],['b',12],['r',20],['q',40]]
                        for typ in types:
                            state.board[side][pc]["typ"] = typ[0]
                            state.board[side][pc]["score"] = typ[1]
                            states.append(state)
                        convert = False
        
        squares = ["a3","b3","c3","d3","e3","f3","g3","h3","a6","b6","c6","d6","e6","f6","g6","h6"]
        for state in states:
            for sqr in squares:
                if self.board["is_occupied"][sqr] == "enpass":
                    if state.board["is_occupied"][sqr] == "enpass":
                        state.board["is_occupied"][sqr] = False
                
        
        return states
    """
    checks if the king of the side given as input to the function is under check.
    returns a boolean value True or False for whether the king is under check or not.
    """
    def check_check(self,side):
        if side == 'w':
            oppos_side = 'b'
        else:
            oppos_side = 'w'
            
        set_of_moves = self.covered_squares(oppos_side)["set_of_moves"]
        if self.board[side]["king"]["cr_pos"] in set_of_moves:
            return True
        return False
    
    """
    How AI Scores the board to decide which state to choose.
    This has been created personally, and obviously can be improved.
    returns an integer value scoring the state
    """
    def heuristic(self):
        #Points to check:
        #1)all pieces on board for both sides
        #2)their position(different squares has different values)
        #3)pawn structure
        #4)king safety
        h_val = 0
        pieces =["p1","p2","p3","p4","p5","p6","p7","p8","r1","k1","b1","q","king","b2","k2","r2"]
        piece = []
        temp_board = copy.deepcopy(self.board)
        #print(temp_board)
        #print(temp_board['w']['r1']['typ'])
        board_score = {
            'w': None,
            'b': None
        }
        board_score['w'] = {
            "a1" :0.25,
            "a2" :0.25,
            "a3" :0.25,
            "a4" :0.25,
            "a5" :0.25,
            "a6" :0.25,
            "a7" :0.25,
            "a8" :0.25,
            "b1" :0.25,
            "b2" :0.5,
            "b3" :0.5,
            "b4" :0.5,
            "b5" :0.5,
            "b6" :0.5,
            "b7" :0.5,
            "b8" :0.25,
            "c1" :0.25,
            "c2" :0.5,
            "c3" :0.75,
            "c4" :0.75,
            "c5" :0.75,
            "c6" :0.75,
            "c7" :0.5,
            "c8" :0.25,
            "d1" :0.25,
            "d2" :0.5,
            "d3" :0.75,
            "d4" :1,
            "d5" :1,
            "d6" :0.75,
            "d7" :0.5,
            "d8" :0.25,
            "e1" :0.25,
            "e2" :0.5,
            "e3" :0.75,
            "e4" :1,
            "e5" :1,
            "e6" :0.75,
            "e7" :0.5,
            "e8" :0.25,
            "f1" :0.25,
            "f2" :0.5,
            "f3" :0.75,
            "f4" :0.75,
            "f5" :0.75,
            "f6" :0.75,
            "f7" :0.5,
            "f8" :0.25,
            "g1" :0.25,
            "g2" :0.5,
            "g3" :0.5,
            "g4" :0.5,
            "g5" :0.5,
            "g6" :0.5,
            "g7" :0.5,
            "g8" :0.25,
            "h1" :0.25,
            "h2" :0.25,
            "h3" :0.25,
            "h4" :0.25,
            "h5" :0.25,
            "h6" :0.25,
            "h7" :0.25,
            "h8" :0.25         
        }
        board_score['b'] = {
            "a1" :0.25,
            "a2" :0.25,
            "a3" :0.25,
            "a4" :0.25,
            "a5" :0.25,
            "a6" :0.25,
            "a7" :0.25,
            "a8" :0.25,
            "b1" :0.25,
            "b2" :0.5,
            "b3" :0.5,
            "b4" :0.5,
            "b5" :0.5,
            "b6" :0.5,
            "b7" :0.5,
            "b8" :0.25,
            "c1" :0.25,
            "c2" :0.5,
            "c3" :0.75,
            "c4" :0.75,
            "c5" :0.75,
            "c6" :0.75,
            "c7" :0.5,
            "c8" :0.25,
            "d1" :0.25,
            "d2" :0.5,
            "d3" :0.75,
            "d4" :1,
            "d5" :1,
            "d6" :0.75,
            "d7" :0.5,
            "d8" :0.25,
            "e1" :0.25,
            "e2" :0.5,
            "e3" :0.75,
            "e4" :1,
            "e5" :1,
            "e6" :0.75,
            "e7" :0.5,
            "e8" :0.25,
            "f1" :0.25,
            "f2" :0.5,
            "f3" :0.75,
            "f4" :0.75,
            "f5" :0.75,
            "f6" :0.75,
            "f7" :0.5,
            "f8" :0.25,
            "g1" :0.25,
            "g2" :0.5,
            "g3" :0.5,
            "g4" :0.5,
            "g5" :0.5,
            "g6" :0.5,
            "g7" :0.5,
            "g8" :0.25,
            "h1" :0.25,
            "h2" :0.25,
            "h3" :0.25,
            "h4" :0.25,
            "h5" :0.25,
            "h6" :0.25,
            "h7" :0.25,
            "h8" :0.25         
        }
        
        material_score = 0
        positional_score = 0
        for piece_name in pieces:
            piece = []
            piece.append(temp_board['w'][piece_name])
            piece.append(temp_board['b'][piece_name])
            #print(piece[0])
            #print(piece[1])
            if piece[0]["on_brd"]:
                
                #print(piece_name,"w:",piece[0]["typ"],material_score,positional_score)
                material_score += piece[0]["score"]
                positional_score += board_score['w'][piece[0]['cr_pos']]
                temp_var = self.pos_moves(piece[0],'w')
                pos_mov = temp_var["pos_pos"]
                protected_squares = temp_var["protects"]
                
                for mov in pos_mov:
                    positional_score += board_score['w'][mov]
                    if self.board["is_occupied"][mov]:
                        piece_side = self.piece_at_pos(mov)
                        piece_k = piece_side["piece"]
                        side = piece_side["side"]
                        positional_score += 0.5*piece_k["score"]
                        positional_score -= board_score['w'][mov]
                            
                for sqr in protected_squares:
                    protected_piece = self.piece_at_pos(sqr)["piece"]
                    if protected_piece["typ"] != "king":
                        positional_score += 0.5*protected_piece["score"]
                    else:
                        positional_score += 10
            
            if piece[1]["on_brd"]:
                #print("b:",piece[1]["typ"],material_score,positional_score)
                material_score -= piece[1]["score"]
                positional_score -= board_score['b'][piece[1]['cr_pos']]
                temp_var = self.pos_moves(piece[1],'b')
                pos_mov = temp_var["pos_pos"]
                protected_squares = temp_var["protects"]
                
                for mov in pos_mov:
                    positional_score -= board_score['b'][mov]
                    if self.board["is_occupied"][mov]:
                        piece_side = self.piece_at_pos(mov)
                        piece_k = piece_side["piece"]
                        side = piece_side["side"]
                        positional_score -= 0.5*piece_k["score"]
                        positional_score += board_score['w'][mov]
                            
                for sqr in protected_squares:
                    protected_piece = self.piece_at_pos(sqr)["piece"]
                    if protected_piece["typ"] != "king":
                        positional_score -= 0.5*protected_piece["score"]
                    else:
                        positional_score -= 10
            
            
        pawn_structure = 0
        pawns = ['p1','p2','p3','p4','p5','p6','p7','p8']
        pawn_pos = {
            'w' : [],
            'b' : []
        }
        for pawn in pawns:
            if temp_board['w'][pawn]['typ'] == 'p':
                if temp_board['w'][pawn]['on_brd']:
                    pawn_pos['w'].append(temp_board['w'][pawn]['cr_pos'])
                    
            if temp_board['b'][pawn]['typ'] == 'p':
                if temp_board['b'][pawn]['on_brd']:
                    pawn_pos['b'].append(temp_board['b'][pawn]['cr_pos'])
                
        pawn_structure += self.pawn_structure_eval(pawn_pos['w'])
        pawn_structure -= self.pawn_structure_eval(pawn_pos['b'])
        
        for pwn_pos in pawn_pos['w']:
            pwn_coord = self.pos_to_coord(pwn_pos)
            check_coord = [pwn_coord[0]+1,pwn_coord[1]]
            check_pos = self.coord_to_pos(check_coord)
            if self.board["is_occupied"][check_pos] ==True:
                pawn_structure -= 0.25
                if self.piece_at_pos(check_pos)["side"] == 'w':
                    pawn_structure -= 0.75
        for pwn_pos in pawn_pos['b']:
            pwn_coord = self.pos_to_coord(pwn_pos)
            check_coord = [pwn_coord[0]-1,pwn_coord[1]]
            check_pos = self.coord_to_pos(check_coord)
            if self.board["is_occupied"][check_pos] ==True:
                pawn_structure += 0.25
                if self.piece_at_pos(check_pos)["side"] == 'b':
                    pawn_structure += 0.75
        if self.board["w"]["king"]["castle"]:
            positional_score += 10
        if self.board["b"]["king"]["castle"]:
            positional_score -= 10
        h_val = positional_score + material_score + pawn_structure
        #print(positional_score, material_score, pawn_structure)
        return h_val
    
    """
    helper function for the heuristic function to score the pawn structure.
    returns an integer value "score" representing the score of the pawn structure.
    """
    def pawn_structure_eval(self,pawn_pos):
        score = 0
        col_set = set()
        col_d_set = set()
        pawn_coord = []
        
        #this part is to check double and triple pawn and reduce score accordingly
        for pwn_pos in pawn_pos:
            prior_len = col_set.__len__()
            col_set = col_set.union(pwn_pos[0])
            post_len = col_set.__len__()
            if prior_len == post_len:
                score -= 1
                prior_d_len = col_d_set.__len__()
                col_d_set = col_d_set.union(pwn_pos[0])
                post_d_len = col_d_set.__len__()
                if prior_d_len == post_d_len:
                    score -= 1.5
    
            pawn_coord.append(self.pos_to_coord(pwn_pos))
        length = pawn_coord.__len__()
        for i in range(length-1):
            for j in range(i+1,length):
                if (abs(pawn_coord[i][1] - pawn_coord[j][1]) == 1):
                    score += 0.25
                    if (abs(pawn_coord[i][0] - pawn_coord[j][0]) == 1):
                        score += 1
                        
        return score
    
    """
    checks if the game has come to an end. (either side wins or looses, or if its a draw.)
    """
    def end_check(self,side):
        set_of_moves = set()
        if side == 'w':
            oppos_side = 'b'
        else:
            oppos_side = 'w'
            
        #win condition
        if (self.pos_moves(self.board[side]["king"],side)["pos_pos"].__len__() == 0):
            set_of_moves = set(self.covered_squares(oppos_side))
            if self.board[side]["king"]["cr_pos"] in set_of_moves:
                return [True,'wins']
        #draw condition
        
        else:
            all_pos = self.piece_pos()
            side_pos = {
                "w" : all_pos["w"],
                "b" : all_pos["b"]
            }
            white_pieces = set()
            black_pieces = set()
        #1)insufficient pieces
            if (side_pos["w"].__len__() <= 2) and (side_pos["w"].__len__() <= 2):
                for pos in side_pos["w"]:
                    white_pieces = white_pieces.union(self.piece_at_pos(pos)["piece"]["typ"])
                for pos in side_pos["b"]:
                    black_pieces = black_pieces.union(self.piece_at_pos(pos)["piece"]["typ"])
                all_pieces = white_pieces.union(black_pieces)
                if not('r' in all_pieces) and not('p' in all_pieces) and not('q' in all_piece):
                    return [True,'draw']
        #2)recurring moves
            """count = 0
            for rec in self.record:
                if self.board == rec["board"] and oppos_side == rec["side"]:
                    count += 1
            if count == 3:
                return [True,'draw']"""
        return [False,'continue']
    
    """This is a function to check the possible squares the given input side can possibly move to."""
    def covered_squares(self,side):
        
        mov_list = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        all_pos = self.piece_pos()[side]
        set_of_moves = set()
        protected_squares = set()
        powers_pos = []
        pawn_pos = []
        for pos in all_pos:
            if self.piece_at_pos(pos)["piece"]["typ"] == "p":
                pawn_pos.append(pos)
            else:
                if self.piece_at_pos(pos)["piece"]["typ"] != "king":
                    powers_pos.append(pos)
                else:
                    king_coord = self.pos_to_coord(pos)
                    temp_mov = [ [king_coord[0] + km[0],king_coord[1] + km[1]] for km in mov_list]
                    for tm in temp_mov:
                        if (8>=tm[0]>=1) and (8>=tm[1]>=1):
                            pos_tm = self.coord_to_pos(tm)
                            if self.board["is_occupied"][pos_tm] == True:
                                if self.piece_at_pos(pos_tm)["side"] != side:
                                    set_of_moves = set_of_moves.union([pos_tm])
                            else:
                                set_of_moves = set_of_moves.union([pos_tm])
                        
        for pwr_pos in powers_pos:
            pos_movs = self.pos_moves(self.piece_at_pos(pwr_pos)["piece"],side)
            set_of_moves = set_of_moves.union(set(pos_movs["pos_pos"]))
            protected_squares = protected_squares.union(set(pos_movs["protects"]))
        for pwn_pos in pawn_pos:
            coord_pos = self.pos_to_coord(pwn_pos)
            if side == 'w':
                if coord_pos[1] == 1:
                    set_of_moves = set_of_moves.union(set([self.coord_to_pos([coord_pos[0]+1,coord_pos[1]+1])]))
                elif coord_pos[1] == 8:
                    set_of_moves = set_of_moves.union(set([self.coord_to_pos([coord_pos[0]+1,coord_pos[1]-1])]))
                else:
                    set_of_moves = set_of_moves.union(set([self.coord_to_pos([coord_pos[0]+1,coord_pos[1]-1]),self.coord_to_pos([coord_pos[0]+1,coord_pos[1]+1])]))
            else:
                if coord_pos[1] == 1:
                    set_of_moves = set_of_moves.union(set([self.coord_to_pos([coord_pos[0]-1,coord_pos[1]+1])]))
                elif coord_pos[1] == 8:
                    set_of_moves = set_of_moves.union(set([self.coord_to_pos([coord_pos[0]-1,coord_pos[1]-1])]))
                else:
                    set_of_moves = set_of_moves.union(set([self.coord_to_pos([coord_pos[0]-1,coord_pos[1]-1]),self.coord_to_pos([coord_pos[0]-1,coord_pos[1]+1])]))
        result = {
            "set_of_moves": list(set_of_moves),
            "protected_squares": list(protected_squares)
        }
        
        return result
    
    """Uses the minimax method, to get the best state from a particular depth given as input,
    if the side to move is given"""
    def minmax_score_at_depth(self,side,depth = 3):
        if side == 'w':
            oppos_side = 'b'
        else:
            oppos_side = 'w'
        root = copy.deepcopy(self)
        node_score = set()
        child_nodes = root.pos_states(side)
        #####################
        #This part was made in attempt to make the code run faster, through parallely running it in multiple threads,
        #Has not been applied in the final code.
        """
        pool = ThreadPool(processes=child_nodes.__len__())
        threads = []
        """
        #####################
        for node in child_nodes:
            
            end = node.end_check(oppos_side)
            if end[0] and (end[1] == 'wins'):
                if side == 'w':
                    node_score = node_score.union([999])
                else:
                    node_score = node_score.union([-999])
            elif end[0] and (end[1] == 'draw'):
                node_score = node_score.union([0])
            else:
                if depth > 1:
                    node_score = node_score.union([node.minmax_score_at_depth(oppos_side,depth-1)])
                else:
                    node_score = node_score.union([node.heuristic()])
        if side == 'w':
            return max(node_score)
        else:
            return min(node_score)
    #####################
    #This part was made in attempt to make the code run faster, through parallely running it in multiple threads,
    #Has not been applied in the final code.
    """def thread_element(self,node,depth,side,oppos_side):
        end = node.end_check(oppos_side)
        if end[0] and (end[1] == 'wins'):
            if side == 'w':
                return [999]
            else:
                return [-999]
        elif end[0] and (end[1] == 'draw'):
            return [0]
        else:
            if depth > 1:
                return [node.minmax_score_at_depth(oppos_side,depth-1)]
            else:
                return [node.heuristic()]"""
    ######################
    
    """
    This function is essentially the driver function, given the side, it decides the optimal move, or gives,
    if a side wins or looses.
    """
    def decide_next_mov(self,side,depth = 1):
        if side == 'w':
            oppos_side = 'b'
        else:
            oppos_side = 'w'
        child_nodes = self.pos_states(side)
        if child_nodes.__len__() == 0:
            return ("No Moves " + side + " Wins!")
        if depth == 1:
            node_score = [node.heuristic() for node in child_nodes]
        else:
            node_score = [node.minmax_score_at_depth(oppos_side,depth-1) for node in child_nodes]
        if side == 'w':
            index = node_score.index(max(node_score))
        else:
            index = node_score.index(min(node_score))
        return child_nodes[index]


# In[3]:


###############Example on how to run#####################
p = chess()
p.init_board()
#p.board["is_occupied"]["a2"] = False
#p.board["w"]["p1"]["on_brd"] = False
#p.board["is_occupied"]["e2"] = False
#p.board["w"]["p5"]["on_brd"] = False
#p.board["is_occupied"]["a8"] = False
#p.board["b"]["r1"]["on_brd"] = False
#p.heuristic()
k = p.decide_next_mov('w',2)
print(k.board)
##########################################################


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





from pgn import ChessParser
from branch import Memory


memory = Memory()
memory.memorize("e4,e5,Nc3,Nc6,Bc4,Nf6,d3,Bc5,f4")
memory.memorize("e4,g6,e5,Bg7,Nc3,d6,Be2")
memory.memorize("e4,c5,a3,Nc3,b4,cxb4,axb4,Nxb4,c3,Nc6,d4,d5,exd5")

parser = ChessParser()

parser.parse(memory,
             "1. e4 e5 2. Nc3 Nc6 3. Bc4 Nf6 (3... Bc5 4. Qg4 { Vienna Copycat Variation }) 4. d3 { Vienna Hybrid } 4... Na5 (4... Bc5) 5. Nge2 Nxc4 6. dxc4 Bc5 7. Qd3 { Vienna Open Variation } *",
             "1 Vienna Max Lange",
             "vienna/")

parser.parse(memory,
             "1. e4 { [%eval 0.25] } 1... e5 { [%eval 0.31] } 2. Nc3 { [%eval 0.12] } 2... Nc6 { [%eval 0.17] } 3. Bc4 { [%eval 0.09] } 3... Nf6 { [%eval 0.0] } 4. d3 { [%eval 0.13] } 4... Bc5 { [%eval 0.13] } 5. f4 { [%eval 0.0] } 5... d6 { [%eval 0.05] } 6. Nf3 { [%eval 0.0] } 6... Bg4 { [%eval 0.13] } (6... h6 7. Na4 Bb6) (6... O-O 7. f5 Na5 8. Bg5 Nxc4 9. dxc4 Bb4) 7. Na4 { [%eval 0.0] } 7... Bxf3 { [%eval 0.5] } (7... Nd4 8. Nxc5 Bxf3 (8... dxc5 9. c3 Bxf3 10. gxf3 Nc6 11. Bb5 a6 12. Bxc6+ bxc6 13. fxe5 Nd7 14. Bf4 O-O) 9. gxf3 dxc5 10. c3 Nc6) (7... Bb6 8. h3 Bxf3 9. Qxf3 Nd4 10. Qf2 Ba5+ (10... Nxc2+ 11. Qxc2) 11. c3 b5 12. O-O bxc4 13. cxd4 exd4 (13... cxd3 14. fxe5 dxe5 15. dxe5) (13... exf4 14. e5 dxe5 15. dxe5 Nd7 16. Bxf4 O-O) 14. Qxd4 cxd3 15. e5 Nd7) (7... exf4) (7... Bb4+ 8. c3 Ba5 9. b4 Bb6 10. Nxb6 axb6 11. h3 Bxf3 12. Qxf3 exf4 13. Bxf4 Ne5 14. Bxe5 dxe5 15. O-O O-O 16. Qg3 Qd6 17. Rf5 b5 18. Bb3 Rae8 19. Raf1) 8. Qxf3 { [%eval -0.25] } 8... Nd4 { [%eval 0.61] } 9. Qd1 { [%eval 0.36] } 9... b5 { [%eval 0.85] } 10. Bxf7+ { [%eval 1.09] } 10... Kxf7 { [%eval 0.74] } 11. Nxc5 { [%eval 0.89] } 11... dxc5 { [%eval 1.12] } (11... exf4 12. Nb3 Ne6 13. a4 Qd7 14. axb5 Qxb5 15. Bd2) 12. fxe5 { [%eval 0.92] } 12... Nd7 { [%eval 1.15] } (12... Ne8 13. O-O+ Ke6 14. Qg4+ Ke7 15. Bg5+ Nf6 16. exf6+ Kd6 17. fxg7) 13. O-O+ { [%eval 1.41] } (13. c3 Ne6 14. O-O+ Ke7 (14... Ke8 { [%cal Gd3d4] } 15. d4 cxd4 16. cxd4 Nxe5 17. Be3 Ng6 18. d5 Ng5) (14... Kg8 15. d4 c4) 15. d4 Rf8 16. d5 Nxe5 17. Rxf8 Kxf8 18. Qh5) 13... Kg8 { [%eval 1.04] } (13... Ke6 14. Qg4+ Kxe5 (14... Ke7 15. Qxg7+ Ke6 16. Qf7+ Kxe5 17. Bf4#) 15. Bf4+ Kf6 16. Bd6+ Nf5 17. Qxf5#) (13... Ke7 14. Bg5+ Ke8 (14... Nf6 15. exf6+ Kd6 16. c3 Ne6 17. Bh4 Qd7 18. d4 (18. a4) 18... cxd4 19. cxd4) 15. Bxd8) (13... Ke8) 14. c3 { [%eval 0.87] } 14... Ne6 { [%eval 1.26] } 15. d4 { [%eval 1.6] } 15... h5 { [%eval 1.71] } (15... h6) (15... cxd4 16. cxd4) 16. d5 { [%eval 1.93] } 16... Nef8 { [%eval 1.78] } (16... Ng5 17. Rf5 Nh7 18. Qf3 Qh4 19. Bf4 Rf8 20. e6 Rxf5 21. exf5 Nb6 22. Bxc7 Ng5 23. Qf4 Qxf4 24. Bxf4 Ne4 25. d6 g5 26. Be5) 17. e6 Ne5 *",
             "2 Vienna Hybrid: Main Line",
             "vienna/")

parser.parse(memory,
             "1. e4 e5 2. Nc3 Nc6 (2... Nf6 3. Nf3) 3. Bc4 d6 (3... Nf6 4. d3 d6 5. a4 (5. f4 Na5 (5... exf4 6. Bxf4 Na5) 6. Nf3 exf4 (6... Nxc4 7. dxc4 Be6 8. Qe2 exf4 9. Bxf4)) 5... Be6 6. Nf3 Bxc4 7. dxc4 Nb4 8. O-O a5 9. Be3 Ng4 (9... Be7 10. Nh4 g6 (10... O-O 11. Nf5 g6 12. Nxe7+ Qxe7 13. Bh6 Rfc8 14. f4 exf4 15. Rxf4 Nd7 16. Qd2 Re8 17. Raf1 f6)) 10. Bd2) 4. a3 (4. Nge2 Nf6 (4... Na5 5. Bd3 c5 6. Bb5+ Bd7 7. a4 Be7 8. O-O { [%cal Ga5c6] } 8... a6 9. Bxd7+ Qxd7 10. d3 Nf6) 5. d4 Nxe4 (5... exd4 6. Nxd4) 6. Nxe4 d5 7. Bg5 f6 (7... Be7 8. Bxe7 Nxe7 9. dxe5 dxc4 10. Qxd8+) (7... Qd7 8. Bb5 dxe4 9. d5 f6 10. O-O fxg5 11. Nc3 a6 12. dxc6 bxc6 13. Qh5+ g6 14. Qxg5 axb5 15. Qxe5+ Kf7 16. Rfd1 Qe7 17. Qxh8 Bg7 18. Qd8 Qxd8 19. Rxd8 Bf6) 8. Bxf6 gxf6 9. Bxd5 Qxd5 (9... f5 10. N4c3) 10. Nxf6+) (4. d3 Nf6 5. f4) (4. Nf3) 4... Nf6 (4... Na5 5. Ba2) 5. d3 Nd4 (5... Be7 6. Nge2) (5... Be6 6. Nf3 Bxc4 7. dxc4 Na5 8. Qe2 Be7 9. Be3 O-O) 6. Nge2 (6. f4) 6... Nxe2 (6... Bg4 7. h3 Nxe2 (7... Bh5 8. Qd2 Bxe2 (8... d5 9. exd5 Nxe2 10. Nxe2 Nxd5 11. Ng3 Bg6 12. Qe2 Bd6 (12... f6)) 9. Nxe2 Nxe2 10. Qxe2 Be7 11. f4 d5 12. exd5 exf4 13. Bxf4 Nxd5 14. Bxd5 Qxd5 15. O-O-O O-O) 8. hxg4 Nxc1 9. Qf3 Nxd3+ 10. cxd3 Be7 11. g5 Ng8 12. Qxf7+ Kd7 13. Be6+ Kc6 14. Rc1 b6 (14... Nh6) (14... b5 15. Nd5+ Kb7 16. Nxc7) 15. Bd5+ Kd7 16. Qf5+ Ke8 17. Bc6+ Qd7 18. Bxd7+ Kd8 19. Bc6 Nf6 20. gxf6 b5 21. Qd7#) 7. Qxe2 c6 (7... Be7 8. h3 O-O) 8. f4 Be7 9. fxe5 Bg4 10. Qf2 dxe5 11. Be3 O-O 12. O-O b5 13. Bb3 c5 14. Nd5 Nxd5 15. Bxd5 *",
             "3. Vienna Hybrid: 3... d6 Vienna Game: Max Lange Defense",
             "vienna/")

parser.parse(memory,
             "1. e4 e5 2. Nc3 Nc6 3. Bc4 Nf6 4. d3 Bb4 5. Ne2 { Vienna Hybrid, Hromádka Variation } 5... d5 6. exd5 Nd4 (6... Nxd5 7. Bd2 Nxc3 (7... Bg4 8. Nxd5 Bxe2 9. Qxe2 Bxd2+ 10. Qxd2) 8. Nxc3 Na5 9. Qe2 Nxc4 10. dxc4 O-O 11. O-O-O Bxc3 12. Bxc3 Qg5+ 13. Bd2 Qxg2 14. Rhg1 Qxh2 15. Rh1 Qg2 16. Rdg1 Bg4 17. Qd3 e4 18. Rxg2 exd3 19. Rxg4 dxc2 20. Bh6 g6 21. Bxf8) 7. a3 Bxc3+ 8. Nxc3 *",
             "4. Vienna Hybrid: 5... Ng2 Bishop's Opening: Vienna Hybrid, Hromádka Variation",
             "vienna/")

parser.parse(memory,
             "1. e4 e5 2. Nc3 Nc6 (2... Nf6 3. Bc4 Nc6 4. d3 Bc5 5. f4 (5. a3 d6 (5... O-O 6. Na4 (6. f4 d6 7. Nf3 Bg4 8. Na4 Bxf3 9. Qxf3 b5 10. Nxc5 bxc4 11. Na4 d5) 6... Be7 7. Nc3 Bc5 (7... d6 8. Nd5)) 6. Na4 Bb6 7. Nxb6 (7. Ne2 O-O) 7... axb6) (5. a4 d6 (5... Bb4 6. Bg5 h6 (6... Bxc3+ 7. bxc3 h6 8. Bh4 d6 9. a5 Be6 (9... g5 10. Bg3 Nh5) 10. Bb5 a6 11. Bxc6+ bxc6) 7. Bxf6 Qxf6 8. Ne2)) 5... exf4 (5... O-O 6. Nf3 d6 (6... Ng4 7. Qe2 Nd4 8. Nxd4 Bxd4 9. Nd5 d6 10. f5 Qh4+ (10... c6 11. Qxg4 cxd5 12. Bh6 Qf6 13. Bg5 Qxg5 (13... Qg6 14. Bxd5 h6 15. fxg6 Bxg4 16. gxf7+ Kh8 17. Be7 Bxb2 18. Rb1 Bd4 19. Bxd6 Rad8 20. Bxf8 Rxf8) 14. Qxg5 dxc4 15. f6 g6 16. Qh6 Kh8 17. Qg7#) (10... Nh6) 11. g3 Qh3 12. Nxc7 Rb8 13. c3 Bf2+ 14. Kd2 b5 15. Bb3 a5 16. Qf1 Qxf1 17. Rxf1) 7. Na4 (7. f5 Na5 8. Bb3 Nxb3 9. axb3 Ng4 10. Qe2) 7... Bb6 8. fxe5 dxe5 9. Nxb6 axb6 10. a3) 6. Bxf4 d6 (6... O-O 7. Nf3 (7. Qd2 Na5 8. O-O-O Nxc4 9. dxc4 d6 10. Nf3 Bg4 11. Bg5 h6 12. Bh4 g5 13. Bxg5 hxg5 14. Qxg5+ Kh7 15. Qh4+ Kg7 16. Qg5+ Kh8 (16... Kh7 17. Qh4+ Kg7 (17... Kg6 18. Nd5 Bxf3 19. gxf3 Nxd5 20. Rhg1+ Bxg1)) 17. Qh6+ (17. Qh4+ Kg8 18. e5 dxe5 19. Qg5+ Kh8) 17... Nh7) 7... d6 8. Qd2 Na5 9. O-O-O Nxc4 10. dxc4 Bb4 11. Rhe1 Be6 12. Bg5 h6 13. Bh4 g5 14. Nxg5 hxg5 15. Qxg5+ Kh8 16. Qh6+ Kg8 17. Bxf6 Qxf6 18. Qxf6 Rfe8 19. Qg5+ Kf8 20. Nd5 Bxe1 21. Qh6+ Kg8 22. Nf6#) 7. Nf3 O-O (7... Nh5 8. Bg5 f6 9. d4 Bb6 10. Be3 Bg4 11. h3 (11. O-O Ne5 12. Be2 O-O 13. Nxe5 fxe5 (13... Bxe2 14. Qxe2) 14. Rxf8+ Qxf8 15. Bxg4) 11... Bxf3 (11... Ng3 12. Rg1) 12. Qxf3 g6 13. O-O-O) (7... Ng4 8. d4 Bb6 9. Bg5 f6 10. Bf4 g5 11. Bc1 Na5 12. Be2 O-O (12... Nc6 13. h3 Nh6 14. Bc4 Ba5 15. Nxg5 fxg5 16. Qh5+) 13. h3 Nh6 14. h4 Ng4 15. hxg5 fxg5 16. Bxg5 Qe8 17. Qd2 Be6 18. Rh4) 8. Qd2 (8. d4 Bb4 (8... Bb6 9. Bg5) 9. Bg5 Bxc3+ 10. bxc3 h6 11. Bh4) 8... Bg4 (8... Nh5 9. Bg5 Qd7 (9... Qe8 10. Nd5 Bb6 11. a4 Ba5 (11... Na5 12. Be7) 12. c3) 10. d4 Bb6 11. O-O-O Na5 12. Be2) (8... Nd4) (8... Be6 9. Bxe6 fxe6) 9. O-O-O Nd4 10. Rdf1 Bxf3 (10... Nxf3 11. gxf3 Bh5) (10... Nh5 11. Bg5 Qd7 12. Nxd4 Bxd4 13. Nd5 (13. Be3 Bxe3 14. Qxe3) 13... h6 (13... f6 14. Nxf6+ Kh8 15. Nxd7) 14. c3 b5 15. Bb3 hxg5 16. Qxg5 Bf6 17. Rxf6 Qd8) 11. gxf3 Re8 12. Rhg1 d5 13. Bxd5 Nxd5 14. Nxd5 Nb5 15. Qg2 (15. Rxg7+ Kxg7 16. Bg5 Qd6 17. Bf6+ Qxf6 18. Nxf6 Kxf6 19. Qf4+ Ke7 20. Qe5+ Kd7 21. Qxc5 c6 22. Qf5+ Ke7) 15... Bxg1 (15... g6 16. Bg5 Qd6) 16. Rxg1 g6 17. Bg5 Qd6 18. Nf6+ Kf8 (18... Kg7 19. Qh3) 19. Qh3 Re6 20. Qh6+ Ke7 21. Re1 Nd4 (21... Rxf6 22. e5) 22. Nd5+ Kd7 23. Qg7) 3. Bc4 Nf6 4. d3 Bc5 (4... d6 5. f4) 5. f4 exf4 6. Bxf4 d6 (6... O-O 7. Nf3 d6 8. Qd2 Be6 9. Bb3 Na5 10. Bxe6 fxe6 11. O-O-O e5 12. Bg5 h6 13. Bxf6 Qxf6 (13... Rxf6 14. Nd5 Rxf3 15. gxf3) 14. Nd5 Qf7) 7. Qd2 O-O (7... Ng4 8. Nf3 Bf2+ 9. Kd1 Bb6 10. d4 Na5) 8. O-O-O Nd4 (8... Be6) (8... a6 9. Rf1 Nd4 10. Bg5 c6 11. Bxf6 gxf6 12. a3 b5 13. Ba2 Be6 14. Qh6 Bxa2 15. Nxa2) (8... Ng4 9. Nf3 Nf2 10. Bg5 Ne7 11. Nd5 Nxd5 12. Bxd8 Be3 13. Bxd5 Nxd1 14. Kxd1 (14. Bxc7 Bxd2+ 15. Kxd2 Nxb2 16. Bxd6 Rd8 17. Be7 Rxd5 18. exd5)) 9. Nf3 Bg4 (9... Nxf3 10. gxf3) 10. Rhf1 (10. Ne2 Bxf3 11. gxf3 Nxf3 12. Qc3 b5 { [%cal Gd3d4] } (12... Nh5 13. d4 Nxd4 14. Rxd4 Nxf4 15. Nxf4 Bxd4 16. Qxd4 Qg5) 13. d4 Nxd4 14. Nxd4 bxc4) 10... Bxf3 11. gxf3 Ne6 12. Be3 Bxe3 13. Qxe3 a6 14. d4 b5 15. Bb3 b4 16. Nd5 Nxd5 17. exd5 (17. Bxd5) *",
             "5. Vienna Hybrid: 5... exf4",
             "vienna/")

parser.parse_file("input/lichess_study_modern-games_by_guilherme_silveira_2023.09.17.pgn",
                  memory,
                  "modern/")

parser.parse_file("input/lichess_study_sicilian-gambit_by_guilherme_silveira_2023.09.20 (1).pgn",
                  memory,
                  "sicilian/")

# parser.parse(memory,
#              "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Be3 a6 5. Qd2 Nd7 6. O-O-O b5 *",
#              "1. Modern white queen castler",
#              "modern/")

# parser.parse(memory,
#              "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Be3 a6 5. Qd2 Nd7 6. f3 b5 { Rare situation } *",
#              "2. Modern white f3 defender",
#              "modern/")

# parser.parse(memory,
#              "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Be3 a6 5. Qd2 Nd7 6. f3 b5 7. a4 b4 8. Nd5 a5 (8... c5 9. dxc5 dxc5 10. O-O-O e6 11. Bg5 Qa5 12. Ne3 Qxa4 13. Kb1 Ngf6) 9. O-O-O Bb7 *",
#              "3. Modern white f3 defender a4 fighter",
#              "modern/")

# parser.parse(memory,
#              "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Be3 a6 5. Qd2 Nd7 6. f3 b5 7. a4 b4 8. Nd1 Ngf6 9. Qxb4 c5 10. Qd2 (10. dxc5 Rb8 11. Qd2 Nxc5) 10... O-O *",
#              "4. Modern white f3 defender a4 Nd1 queen attack",
#              "modern/")

# parser.parse(memory,
#              "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Be3 a6 5. Qd2 Nd7 6. f3 b5 7. a4 b4 8. Nd1 c5 9. d5 Ne5 10. Nf2 f5 *",
#              "5. Modern white f3 defender Houdini",
#              "modern/")

# parser.parse(memory,
#              "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Be3 a6 5. Qd2 Nd7 6. f3 b5 7. a4 b4 8. Nd1 c5 9. c3 (9. dxc5 dxc5) 9... bxc3 10. bxc3 Ngf6 *",
#              "6. Modern white f3 defender a4 Nd1 Eichlar Hillarp",
#              "modern/")

# parser.parse(memory,
#              "1. e4 c5 2. a3 Nc6 3. b4 cxb4 4. axb4 Nxb4 5. c3 Nc6 6. d4 d5 7. exd5 Qxd5 8. Na3 a6 9. Nc4 Qd8 10. d5 b5 11. dxc6 Qxd1+ 12. Kxd1 bxc4 13. Nf3 *",
#              "Sicilian Gambit: Accepted a6",
#              "sicilian/")

# parser.parse(memory,
#              "1. e4 c5 2. a3 Nc6 3. b4 cxb4 4. axb4 Nxb4 5. c3 Nc6 6. d4 d5 7. exd5 Qxd5 8. Na3 Bf5 9. Nb5 Qd8 10. d5 Ne5 11. Bf4 f6 12. Nf3 a6 13. Nbd4 Nxf3+ 14. Qxf3 Bd7 15. Bc4 *",
#              "Sicilian Gambit: Accepted Bf5",
#              "sicilian/")

# parser.parse(memory,"",
#             "",
#             "modern/")

# parser.parse(memory,"",
#             "",
#             "modern/")

# parser.parse(memory,"",
#             "",
#             "modern/")

# parser.parse(memory,"",
#             "")

# parser.parse(memory,"",
#             "")

# parser.parse(memory,"",
#             "")

# parser.parse(memory,"",
#             "")

# parser.parse(memory,"",
#             "")

# parser.parse(memory,"",
#             "")

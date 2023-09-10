from pgn import parse_chess

# Test
parse_chess("1. e4 e5 2. Nc3 Nc6 { C25 Vienna Game: Max Lange Defense } 3. Bc4 Nf6 (3... Bc5 4. Qg4 { Vienna Copycat Variation }) 4. d3 { Vienna Hybrid } 4... Na5 (4... Bc5) 5. Nge2 Nxc4 6. dxc4 Bc5 7. Qd3 { Vienna Open Variation } *",
            core_key="1 Vienna Max Lange")

parse_chess("1. e4 { [%eval 0.25] } 1... e5 { [%eval 0.31] } 2. Nc3 { [%eval 0.12] } 2... Nc6 { [%eval 0.17] } 3. Bc4 { [%eval 0.09] } 3... Nf6 { [%eval 0.0] } 4. d3 { [%eval 0.13] } 4... Bc5 { [%eval 0.13] } 5. f4 { [%eval 0.0] } 5... d6 { [%eval 0.05] } 6. Nf3 { [%eval 0.0] } 6... Bg4 { [%eval 0.13] } (6... h6 7. Na4 Bb6) (6... O-O 7. f5 Na5 8. Bg5 Nxc4 9. dxc4 Bb4) 7. Na4 { [%eval 0.0] } 7... Bxf3 { [%eval 0.5] } (7... Nd4 8. Nxc5 Bxf3 (8... dxc5 9. c3 Bxf3 10. gxf3 Nc6 11. Bb5 a6 12. Bxc6+ bxc6 13. fxe5 Nd7 14. Bf4 O-O) 9. gxf3 dxc5 10. c3 Nc6) (7... Bb6 8. h3 Bxf3 9. Qxf3 Nd4 10. Qf2 Ba5+ (10... Nxc2+ 11. Qxc2) 11. c3 b5 12. O-O bxc4 13. cxd4 exd4 (13... cxd3 14. fxe5 dxe5 15. dxe5) (13... exf4 14. e5 dxe5 15. dxe5 Nd7 16. Bxf4 O-O) 14. Qxd4 cxd3 15. e5 Nd7) (7... exf4) (7... Bb4+ 8. c3 Ba5 9. b4 Bb6 10. Nxb6 axb6 11. h3 Bxf3 12. Qxf3 exf4 13. Bxf4 Ne5 14. Bxe5 dxe5 15. O-O O-O 16. Qg3 Qd6 17. Rf5 b5 18. Bb3 Rae8 19. Raf1) 8. Qxf3 { [%eval -0.25] } 8... Nd4 { [%eval 0.61] } 9. Qd1 { [%eval 0.36] } 9... b5 { [%eval 0.85] } 10. Bxf7+ { [%eval 1.09] } 10... Kxf7 { [%eval 0.74] } 11. Nxc5 { [%eval 0.89] } 11... dxc5 { [%eval 1.12] } (11... exf4 12. Nb3 Ne6 13. a4 Qd7 14. axb5 Qxb5 15. Bd2) 12. fxe5 { [%eval 0.92] } 12... Nd7 { [%eval 1.15] } (12... Ne8 13. O-O+ Ke6 14. Qg4+ Ke7 15. Bg5+ Nf6 16. exf6+ Kd6 17. fxg7) 13. O-O+ { [%eval 1.41] } (13. c3 Ne6 14. O-O+ Ke7 (14... Ke8 { [%cal Gd3d4] } 15. d4 cxd4 16. cxd4 Nxe5 17. Be3 Ng6 18. d5 Ng5) (14... Kg8 15. d4 c4) 15. d4 Rf8 16. d5 Nxe5 17. Rxf8 Kxf8 18. Qh5) 13... Kg8 { [%eval 1.04] } (13... Ke6 14. Qg4+ Kxe5 (14... Ke7 15. Qxg7+ Ke6 16. Qf7+ Kxe5 17. Bf4#) 15. Bf4+ Kf6 16. Bd6+ Nf5 17. Qxf5#) (13... Ke7 14. Bg5+ Ke8 (14... Nf6 15. exf6+ Kd6 16. c3 Ne6 17. Bh4 Qd7 18. d4 (18. a4) 18... cxd4 19. cxd4) 15. Bxd8) (13... Ke8) 14. c3 { [%eval 0.87] } 14... Ne6 { [%eval 1.26] } 15. d4 { [%eval 1.6] } 15... h5 { [%eval 1.71] } (15... h6) (15... cxd4 16. cxd4) 16. d5 { [%eval 1.93] } 16... Nef8 { [%eval 1.78] } (16... Ng5 17. Rf5 Nh7 18. Qf3 Qh4 19. Bf4 Rf8 20. e6 Rxf5 21. exf5 Nb6 22. Bxc7 Ng5 23. Qf4 Qxf4 24. Bxf4 Ne4 25. d6 g5 26. Be5) 17. e6 Ne5 *",
            core_key="2 Vienna Hybrid: Main Line")

parse_chess("1. e4 e5 2. Nc3 Nc6 (2... Nf6 3. Nf3) 3. Bc4 d6 (3... Nf6 4. d3 d6 5. a4 (5. f4 Na5 (5... exf4 6. Bxf4 Na5) 6. Nf3 exf4 (6... Nxc4 7. dxc4 Be6 8. Qe2 exf4 9. Bxf4)) 5... Be6 6. Nf3 Bxc4 7. dxc4 Nb4 8. O-O a5 9. Be3 Ng4 (9... Be7 10. Nh4 g6 (10... O-O 11. Nf5 g6 12. Nxe7+ Qxe7 13. Bh6 Rfc8 14. f4 exf4 15. Rxf4 Nd7 16. Qd2 Re8 17. Raf1 f6)) 10. Bd2) 4. a3 (4. Nge2 Nf6 (4... Na5 5. Bd3 c5 6. Bb5+ Bd7 7. a4 Be7 8. O-O { [%cal Ga5c6] } 8... a6 9. Bxd7+ Qxd7 10. d3 Nf6) 5. d4 Nxe4 (5... exd4 6. Nxd4) 6. Nxe4 d5 7. Bg5 f6 (7... Be7 8. Bxe7 Nxe7 9. dxe5 dxc4 10. Qxd8+) (7... Qd7 8. Bb5 dxe4 9. d5 f6 10. O-O fxg5 11. Nc3 a6 12. dxc6 bxc6 13. Qh5+ g6 14. Qxg5 axb5 15. Qxe5+ Kf7 16. Rfd1 Qe7 17. Qxh8 Bg7 18. Qd8 Qxd8 19. Rxd8 Bf6) 8. Bxf6 gxf6 9. Bxd5 Qxd5 (9... f5 10. N4c3) 10. Nxf6+) (4. d3 Nf6 5. f4) (4. Nf3) 4... Nf6 (4... Na5 5. Ba2) 5. d3 Nd4 (5... Be7 6. Nge2) (5... Be6 6. Nf3 Bxc4 7. dxc4 Na5 8. Qe2 Be7 9. Be3 O-O) 6. Nge2 (6. f4) 6... Nxe2 (6... Bg4 7. h3 Nxe2 (7... Bh5 8. Qd2 Bxe2 (8... d5 9. exd5 Nxe2 10. Nxe2 Nxd5 11. Ng3 Bg6 12. Qe2 Bd6 (12... f6)) 9. Nxe2 Nxe2 10. Qxe2 Be7 11. f4 d5 12. exd5 exf4 13. Bxf4 Nxd5 14. Bxd5 Qxd5 15. O-O-O O-O) 8. hxg4 Nxc1 9. Qf3 Nxd3+ 10. cxd3 Be7 11. g5 Ng8 12. Qxf7+ Kd7 13. Be6+ Kc6 14. Rc1 b6 (14... Nh6) (14... b5 15. Nd5+ Kb7 16. Nxc7) 15. Bd5+ Kd7 16. Qf5+ Ke8 17. Bc6+ Qd7 18. Bxd7+ Kd8 19. Bc6 Nf6 20. gxf6 b5 21. Qd7#) 7. Qxe2 c6 (7... Be7 8. h3 O-O) 8. f4 Be7 9. fxe5 Bg4 10. Qf2 dxe5 11. Be3 O-O 12. O-O b5 13. Bb3 c5 14. Nd5 Nxd5 15. Bxd5 *",
            "3. Vienna Hybrid: 3... d6 Vienna Game: Max Lange Defense")

parse_chess("1. e4 e5 2. Nc3 Nc6 3. Bc4 Nf6 4. d3 Bb4 5. Ne2 { Vienna Hybrid, Hromádka Variation } 5... d5 6. exd5 Nd4 (6... Nxd5 7. Bd2 Nxc3 (7... Bg4 8. Nxd5 Bxe2 9. Qxe2 Bxd2+ 10. Qxd2) 8. Nxc3 Na5 9. Qe2 Nxc4 10. dxc4 O-O 11. O-O-O Bxc3 12. Bxc3 Qg5+ 13. Bd2 Qxg2 14. Rhg1 Qxh2 15. Rh1 Qg2 16. Rdg1 Bg4 17. Qd3 e4 18. Rxg2 exd3 19. Rxg4 dxc2 20. Bh6 g6 21. Bxf8) 7. a3 Bxc3+ 8. Nxc3 *",
            "4. Vienna Hybrid: 5... Ng2 Bishop's Opening: Vienna Hybrid, Hromádka Variation")

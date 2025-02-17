TO RUN C++ CODE 

g++ -o jwks_server main.cpp -lcrow -lssl -lcrypto -ljwt-cpp -lgtest -pthread
./jwks_server


TO RUN TESTS USING GOOGLE TEXT
./jwks_server --gtest_output=xml:report.xml



# Cyrex Vacancy API Load Test

## Description

This is a gRPC API server load test using locust. It simulates users CRUD behaviour on the server.

## Getting Started

### Dependencies

The API was tested on Linux Ubuntu 20.04 and Python 3.10.4.

- Python 3.8+
- Locust
- BloomRPC Client
- Other dependencies are in the requirements.txt and are installed during the build

### Building script dependencies
```
make gen (Do this if you have not generated protobufs from the proto files)
```
NB: There was this gotcha of having to fix the absolute imports of some probufs otherwise there would be module import error

### Running the script locally

- Check the .env-example file to create a .env file.

On Linux

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Ensure you run the command at the root of the project.

```
make run
```

### Running the app with docker-compose

You can run the script with docker-compose using the command
Build and run the image, do this if it's first time

```
make compose-build
```
or

```
make compose-run
```

### Reports
Response time (the files with latest) and failure reports can be found here [reports](https://github.com/joshajiniran/cryex-task/tree/main/reports)

### Cleanup
To clear the generated protobufs, run:
```
make clean
```

## Help

If you encounter any problem while building, kindly reach out through issues on [GitHub](https://github.com/joshajiniran/cyrex-task.git)

## Authors

Contributors names and contact info

Joshua Ajiniran
josuajiniran@gmail.com

## Version History

- 0.1.1 (coming)
  - Run script headless
  - Find fix for generated protobufs Python import issues
- 0.1.0
  - Initial Release

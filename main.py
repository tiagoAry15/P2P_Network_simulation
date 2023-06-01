from file_util import FileUtil
from graph_util import GraphBuilder


# Press the green button in the gutter to run the script.

def main():
    fileUtil = FileUtil('input_example.txt')
    graphBuilder = GraphBuilder()

    file_content = fileUtil.read()
    print(file_content)

    graph = graphBuilder.build(file_content)
    if graph:
        print(graph.nodes)
        print(graph.edges)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def prints(data=None, result=None, flow=None):
    if data is not None:
        if type(data).__name__ == 'dict':
            print(f"{data['name']} =>")
            data = data['matrix']
        else:
            print("Matrix => ")

        for x in data:
            print(x)
        print()

    if flow is not None:
        if type(flow[0]).__name__ == 'list':
            for x in flow:
                print(x)
        else:
            print("\n".join(flow))
        print()
    if result is not None:
        if type(result).__name__ == 'int':
            print("Result = ", result)
        else:
            print("Result =>")
            for x in result:
                print(x)
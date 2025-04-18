<?php

header('Content-type: application/json');

$request = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

var_dump($request);

switch($request){
    case '/api':
        echo json_encode(['Message' => 'Api funcionando']);
        break;
    case '/api/hello':
        echo json_encode(["message" => "Olá, mundo!"]);
        break;
    default:
        http_response_code(404);
        echo json_encode(["error" => "Endpoint não encontrado"]);
        break;
}
